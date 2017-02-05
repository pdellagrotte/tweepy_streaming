import json
import pandas as pd
import matplotlib.pyplot as plt

plt.interactive(False)

tweets_data_path = 'C:/../twitter_data.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

#tweets['child'] = map(lambda tweet: tweet.get('grandparent', {}).get('parent', {}).get('child') , tweets_data)

print tweet["user"]["name"]

tweets = pd.DataFrame()

tweets['name'] =  map(lambda tweet: tweet.get('user', {}).get('name'),tweets_data)
tweets['text'] = map(lambda tweet: tweet.get('text', None),tweets_data)
tweets['lang'] = map(lambda tweet: tweet.get('lang', None),tweets_data)
tweets['location'] = map(lambda tweet: tweet.get('user', {}).get('location'),tweets_data)
#tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)


tweets_by_lang = tweets['location'].value_counts()
print tweets_by_lang

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
tweets_by_lang[:5].plot(ax=ax, kind='bar', color='blue')

plt.show()
