from time import time
import csv

tweets = []

global_start = time()
for i in range(1, 3001):
    print(f"Counting {i}/3000")
    with open(f"User_Tweets/{i}.csv", "r", newline='') as fp:
        reader = csv.reader(fp)
        user_tweets = list(reader)
        # user_tweets = [x[2]+'\n' for x in user_tweets]
        user_tweets = [[x[2]] for x in user_tweets]
        tweets += user_tweets

print(f"Writing {len(tweets)} tweets to disk. . .")
start_time = time()
'''
with open("LDA_Input/All_Tweets.csv", "w", newline='') as f:
    f.writelines(tweets)
'''
with open("LDA_Input/All_Tweets.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(tweets)

print("All Tweets Saved to a single file.\nTime_Taken:", time() - start_time, "\nTotal Time:", time() - global_start)
