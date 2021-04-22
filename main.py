import tweepy as twitter 
import keys
import time, datetime

auth = twitter.OAuthHandler(keys.API_KEY, keys.API_SECRET_KEY)
auth.set_access_token(keys.ACCESS_TOKEN, keys.SECRET_ACCESS_TOKEN)

api = twitter.API(auth)


def twitterbot(hashtag, delay):
    while True:
        print(f"\n {datetime.datetime.now()}\n")

        for tweet in twitter.Cursor(api.search, q=hashtag, rpp=10).items(50):
            try:
                tweet_id = dict(tweet._json)["id"]
                tweet_text = dict(tweet._json)["text"]

                print(f"id: {str(tweet_id)}")
                print(f"text: {str(tweet_text)}")

                api.retweet(tweet_id)
            
            except twitter.TweepError as error:
                print(error.reason)
        
        time.sleep(delay)

twitterbot("COVIDBeds", 10)