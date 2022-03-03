import pandas as pd
from app.core.models.TwitterServices import TwitterServices


class Hashtags(TwitterServices):

    @classmethod
    def _format_hashtag_search_results(cls, raw_results: dict, user_fields: list) -> list:
        formatted_results = []

        # assemble tweets df
        tweets_df = pd.DataFrame(raw_results.get('data', []))

        # only continue if results exist
        if len(tweets_df) > 0:
            public_metrics = tweets_df.public_metrics.apply(pd.Series)
            tweets_df = tweets_df[[c for c in tweets_df.columns if c not in [
                'public_metrics', 'entities']]]

            # assemble users df
            users = pd.DataFrame(raw_results.get(
                'includes', {}).get('users', []))
            if len(users) == 0:
                users = pd.DataFrame(columns=user_fields)
            users = users.rename({'id': 'author_id'}, axis=1)

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
            result_df = result_df.merge(users, how='left', on='author_id')

            # reformat created_at column
            result_df = result_df.assign(
                created_at=result_df.created_at.apply(cls.reformat_datetime))

            # iterate to form result array
            for _, row in result_df.iterrows():
                formatted_results.append({
                    'account': {
                        'fullname': row['name'],
                        'href': f'/{row.username}',
                        'id': row.author_id,
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
    def search(cls, hashtag: str, limit: int) -> list:
        user_fields = ['id', 'name', 'username']
        query_params = {
            'query': f'#{hashtag}',
            'tweet.fields': 'author_id,created_at,public_metrics,entities',
            'expansions': 'author_id',
            'user.fields': ','.join(user_fields),
            'max_results': limit
        }

        # execute search
        raw_results = cls.execute_query(cls.search_recent_url, query_params)

        # format results
        formatted_results = cls._format_hashtag_search_results(
            raw_results, user_fields)

        return formatted_results


# module testing
if __name__ == '__main__':
    from pprint import pprint
    hashtag = 'python'
    limit = 10

    results = Hashtags.search(hashtag, limit)
    print('------------------------------------------------------------')
    pprint(results)
