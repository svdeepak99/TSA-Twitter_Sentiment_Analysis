# Source Link: https://betterprogramming.pub/how-to-scrape-tweets-with-snscrape-90124ed006af
# Note: The code has resumable capability, so it can be resumed if any interruption of hanging occurs

import snscrape.modules.twitter as sntwitter
import csv
from multiprocessing import Pool
import os

from time import time, sleep


def scrape_user(param):
    try:
        number, dname = param

        # Creating list to append tweet data to
        tweets_list1 = []

        for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f"from:{dname}").get_items()):
            if i >= 3240:
                break
            '''
            if i % 100 == 99 or i == 3239:
                print(f"{i + 1}/3240 Scrapped")
            '''

            # To remove b' ' symbol due to utf-8 end
            tweet_content = str(tweet.content.encode("utf-8"))
            if (tweet_content[:2] == "b'" and tweet_content[-1] == "'") or (
                    tweet_content[:2] == 'b"' and tweet_content[-1] == '"'):
                tweet_content = tweet_content[2:-1]

            tweets_list1.append([tweet.id, tweet.date, tweet_content])
    except:
        while True:
            try:
                number, dname = param

                # Creating list to append tweet data to
                tweets_list1 = []

                for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f"from:{dname}").get_items()):
                    if i >= 3240:
                        break
                    '''
                    if i % 100 == 99 or i == 3239:
                        print(f"{i + 1}/3240 Scrapped")
                    '''

                    # To remove b' ' symbol due to utf-8 end
                    tweet_content = str(tweet.content.encode("utf-8"))
                    if (tweet_content[:2] == "b'" and tweet_content[-1] == "'") or (
                            tweet_content[:2] == 'b"' and tweet_content[-1] == '"'):
                        tweet_content = tweet_content[2:-1]

                    tweets_list1.append([tweet.id, tweet.date, tweet_content])
                break
            except:
                continue

    try:
        with open(f"User_Tweets/{number}.csv", "w", newline='') as fp:
            write = csv.writer(fp)
            write.writerows(tweets_list1)
    except:
        while True:
            try:
                with open(f"User_Tweets/{number}.csv", "w", newline='') as fp:
                    write = csv.writer(fp)
                    write.writerows(tweets_list1)
                break
            except:
                continue


if __name__ == '__main__':
    start_time = time()

    with open("All_Users.csv", "r", newline='') as f:
        reader = csv.reader(f)
        users = list(reader)

    # taskList = [(x[0], x[2]) for x in users]
    taskList = []
    for ui in users:
        if not os.path.isfile(f"User_Tweets/{ui[0]}.csv"):
            taskList.append((ui[0], ui[2]))
    print(f"Mining {len(taskList)} Users. . .")

    process = Pool(60)
    process.map(scrape_user, taskList)
    process.close()
    process.join()

    # JiLin_Tweets

    print("All Tweets Saved, Time Taken:", time() - start_time)
