# To Install: pip install git+https://github.com/JustAnotherArchivist/snscrape.git
# Instructions: https://betterprogramming.pub/how-to-scrape-tweets-with-snscrape-90124ed006af

import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "the OR i OR to OR a OR and OR is OR in OR it OR you OR of OR for OR on OR my OR s OR that OR at OR with OR me OR do OR have OR just OR this OR be OR n’t OR so OR are OR m OR not OR was OR but OR out OR up OR what OR now OR new OR from OR your OR like"

# Creating list to append tweet data to
tweets_list2 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i, tweet in enumerate(
        sntwitter.TwitterSearchScraper(query + ' since:2009-01-01 until:2009-12-31').get_items()):
    if i > 10:
        break
    tweets_list2.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
    print([tweet.date, tweet.id, tweet.content, tweet.user.username])


