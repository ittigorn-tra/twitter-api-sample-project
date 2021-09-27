<!-----
NEW: Check the "Suppress top comment" option to remove this info from the output.

Conversion time: 0.776 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β31
* Mon Sep 27 2021 06:12:34 GMT-0700 (PDT)
* Source doc: Requirements
* Tables are currently converted to HTML tables.
----->



# Twitter API Sample Project


#### Project description:

The main job will be to develop two RESTful API endpoints to provide data from Twitter.

You can get data from Twitter by Twitter API or scraping in real-time.


#### Notes:



* The repository should have a readme file with clear instructions of how to deploy/install locally
* DON’t use public available Twitter SDK instead please implement your own
* Include unit tests

1. Get tweets by a hashtag. Get the list of tweets with the given hashtag.

Optional parameters:

- limit: integer, specifies the number of tweets to retrieve, the default should be 30


#### Example request:

`curl -H "Accept: application/json" -X GET h ttp://localhost:xxxx/hashtags/Python?limit=40`


#### Example response:


```
[
    {
        "account": {
            "fullname": "Raymond Hettinger",
            "href": "/raymondh",
            "id": 14159138
        },
        "date": "12:57 PM - 7 Mar 2018",
        "hashtags": [
            "#python"
        ],
        "likes": 169,
        "replies": 13,
        "retweets": 27,
        "text": "Historically, bash filename pattern matching was known as \"globbing\". Hence, the #python module called \"glob\".\n\n>>> print(glob.glob('*.py')\n\nIf the function were being added today, it would probably be called os.path.expand_wildcards('*.py') which would be less arcane."
    }
]
```


2. Get user tweets. Get the list of tweets that the user has on his feed in JSON format.

Optional parameters:

- limit: integer, specifies the number of tweets t o retrieve, the default should be 30


#### Example request:

`curl -H "Accept: application/json" -X GET h ttp://localhost:xxxx/users/twitter?limit=20`


#### Example response:


```
[
    {
        "account": {
            "fullname": "Twitter",
            "href": "/Twitter",
            "id": 783214
        },
        "date": "2:54 PM - 8 Mar 2018",
        "hashtags": [
            "#InternationalWomensDay"
        ],
        "likes": 287,
        "replies": 17,
        "retweets": 70,
        "text": "Powerful voices. Inspiring women.\n\n#InternationalWomensDay https://twitter.com/i/moments/971870564246634496"
    }
]
```

