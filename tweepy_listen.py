
# 2-5-2017
# Replace empty key strings with API tokens

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

write_path =  'C:/../twitter_data.txt'
i = 0

class StdOutListener(StreamListener):

    def on_data(self, data):
        i = 0
        #print data
        print i
        i += 1
        with open(write_path,'a') as tf:
            tf.write(data)
        return True

    def on_error(self, status):
        print status



if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
        l = StdOutListener()
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        stream = Stream(auth, l)

        #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
        stream.filter(track=['key words'])


