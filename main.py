import json
import logging
import os
import time

import tweepy
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger()
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")


class StdOutListener(tweepy.Stream):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """

    def on_data(self, data):
        j = json.loads(data)
        if 'created_at' in j.keys():
            with open('fetched_tweets.txt', 'a') as tf:
                print(j)
                if not j["truncated"]:
                    tf.write(f"{json.dumps(j)}\n")
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    stream = StdOutListener(consumer_key, consumer_secret, access_token, access_token_secret)

    # auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # auth.set_access_token(access_token, access_token_secret)
    # stream.filter(threaded=True, track=["#Thierryisgevaccineerd"])
    start = time.time()

    open('fetched_tweets.txt', 'w')
    stream.filter(threaded=True, locations=[4.61, 52.27, 5.07, 52.50])

#     user_id = "904811170372169728"
#     tweet_id = "1228393702244134912"
#     liked_tweets = client.get_liked_tweets(id=user_id)
#     print(len(liked_tweets.data))
