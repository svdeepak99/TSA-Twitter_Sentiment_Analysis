# Source Link: https://betterprogramming.pub/how-to-scrape-tweets-with-snscrape-90124ed006af

import snscrape.modules.twitter as sntwitter
import csv

from time import time
start_time = time()

# Creating list to append tweet data to
tweets_list1 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i, tweet in enumerate(sntwitter.TwitterSearchScraper('from:jack').get_items()):
    if i >= 100:
        break
    if i % 100 == 99 or i == 3239:
        print(f"{i + 1}/3240 Scrapped")

    # To remove b' ' symbol due to utf-8 end
    tweet_content = str(tweet.content.encode("utf-8"))
    if (tweet_content[:2] == "b'" and tweet_content[-1] == "'") or (tweet_content[:2] == 'b"' and tweet_content[-1] == '"'):
        tweet_content = tweet_content[2:-1]

    tweets_list1.append([tweet.date, tweet.id, tweet_content, tweet.user.username])


# Creating a dataframe from the tweets list above
with open("jack_Tweets.csv", "w", newline='') as fp:
    write = csv.writer(fp)
    write.writerows(tweets_list1)

with open("jack_Tweets.csv", "r", newline='') as fp:
    read = csv.reader(fp)
    contents = list(read)

for tweet in contents:
    print(tweet[2].encode('utf-8'))

# JiLin_Tweets

print("All Tweets Saved, Time Taken:", time() - start_time)
