import csv
from time import time
from datetime import datetime

start_time = time()

with open("All_Users.csv", "r", newline='') as f:
    reader = csv.reader(f)
    user_data = list(reader)

print(f"Writing for {len(user_data)} users. . .")

for i in range(1, 3001):
    print(f"Counting {i}/3000")
    with open(f"User_Tweets/{i}.csv", "r", newline='') as fp:
        reader = csv.reader(fp)
        tweets = list(reader)
        count = len(tweets)
        user_data[i-1].append(count)
        if count == 0:
            user_data[i - 1] += [0, 0]
            continue
        last_tweet_date = datetime.strptime(tweets[0][1], "%Y-%m-%d %H:%M:%S%z")
        first_tweet_date = datetime.strptime(tweets[-1][1], "%Y-%m-%d %H:%M:%S%z")
        delta = last_tweet_date - first_tweet_date
        duration = delta.days + (delta.seconds / 86400)
        if duration < 30 and count != 3240:
            duration = 30
        user_data[i - 1].append(duration)
        user_data[i - 1].append((30*count)/duration)


with open("Users_Count.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(user_data)

print("Total time taken:", time() - start_time)
