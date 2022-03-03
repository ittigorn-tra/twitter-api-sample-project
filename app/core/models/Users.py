import pandas as pd
from app.core.models.TwitterServices import TwitterServices


class Users(TwitterServices):

    @classmethod
    def _format_user_search_results(cls, raw_results: dict) -> list:
        formatted_results = []

        # assemble tweets df
        tweets_df = pd.DataFrame(raw_results.get('data', []))

        # only continue if results exist
        if len(tweets_df) > 0:
            public_metrics = tweets_df.public_metrics.apply(pd.Series)
            tweets_df = tweets_df[[c for c in tweets_df.columns if c not in [
                'public_metrics', 'entities']]]

            # assemble hashtags series
            hashtags_data = []
            for tweet in raw_results.get('data', []):
                hashtags_this_tweet = []
                for hashtag_obj in tweet.get('entities', {}).get('hashtags', []):
                    if 'tag' in hashtag_obj:
                        hashtags_this_tweet.append(f'#{hashtag_obj["tag"]}')
                hashtags_data.append(hashtags_this_tweet)
            hashtags = pd.Series(hashtags_data)

            # merge tweets and user info
            result_df = tweets_df.join(public_metrics)
            result_df = result_df.assign(hashtags=hashtags)

            # reformat created_at column
            result_df = result_df.assign(
                created_at=result_df.created_at.apply(cls.reformat_datetime))

            # get user info
            user_info = raw_results.get('includes', {}).get('users', [])[0] if len(
                raw_results.get('includes', {}).get('users', [])) > 0 else {}

            # iterate to form result array
            for _, row in result_df.iterrows():
                formatted_results.append({
                    'account': {
                        'fullname': user_info.get('name', ''),
                        'href': f'/{user_info.get("username", "")}',
                        'id': user_info.get('id'),
                    },
                    'date': row.created_at,
                    'hashtags': row.hashtags,
                    'likes': row.like_count,
                    'replies': row.reply_count,
                    'retweets': row.retweet_count,
                    'text': row.text,
                })

        return formatted_results

    @classmethod
    def search_tweets_by_user_id(cls, user_id: str, limit: int, exclude_retweets: bool, exclude_replies: bool) -> list:
        user_fields = ['id', 'name', 'username']
        query_params = {
            'tweet.fields': 'author_id,created_at,public_metrics,entities',
            'expansions': 'author_id',
            'user.fields': ','.join(user_fields),
            'max_results': limit
        }

        # process excludes
        excludes = []
        if exclude_retweets:
            excludes.append('retweets')
        if exclude_replies:
            excludes.append('replies')
        if len(excludes) > 0:
            query_params['exclude'] = ','.join(excludes)

        url = f"https://api.twitter.com/2/users/{user_id}/tweets"

        # execute search
        raw_results = cls.execute_query(url=url, query_params=query_params)

        # format results
        formatted_results = cls._format_user_search_results(raw_results)

        return formatted_results

    @classmethod
    def get_user_id(cls, username: str) -> str:
        user_id = None
        usernames_query = f"usernames={username}"
        user_fields = "user.fields=id"

        url = f"https://api.twitter.com/2/users/by?{usernames_query}&{user_fields}"

        # execute search
        raw_results = cls.execute_query(url=url)
        user_data = raw_results.get('data', [])
        if len(user_data) > 0:
            user_id = user_data[0].get('id')

        return user_id

    @classmethod
    def search_by_username(cls, username: str, limit: int, exclude_retweets: bool, exclude_replies: bool) -> list:
        user_id = cls.get_user_id(username=username)
        results = cls.search_tweets_by_user_id(
            user_id=user_id, limit=limit, exclude_retweets=exclude_retweets, exclude_replies=exclude_replies) if user_id is not None else []
        return results


# module testing
if __name__ == '__main__':
    from pprint import pprint

    # user_id   = '2244994945'
    # limit     = 10
    # results = Users.search_by_id(user_id, limit)
    # print('------------------------------------------------------------')
    # pprint(results)

    username = 'twitter'
    results = Users.get_user_id(username)
    print('------------------------------------------------------------')
    pprint(results)
