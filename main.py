import tweepy as twitter 
import keys
import time, datetime

auth = twitter.OAuthHandler(keys.API_KEY, keys.API_SECRET_KEY)
auth.set_access_token(keys.ACCESS_TOKEN, keys.SECRET_ACCESS_TOKEN)

api = twitter.API(auth)


def twitterbot():

    mentions = api.mentions_timeline(count = 450)

    for tweet in mentions:
        try:
            tweet_id = dict(tweet._json)["id"]
            tweet_text = dict(tweet._json)["text"]

            api.retweet(tweet_id)
        
        except twitter.TweepError as error:
            pass
# if __name__ == "__main__":
while True:
    twitterbot()
    time.sleep(500)