import json
import csv
from datetime import datetime

duration_likes = []

current_time = datetime.strptime("2021-12-01 00:00:01+00:00", "%Y-%m-%d %H:%M:%S%z")
for i in range(1, 3001):
    print(f"Getting attributes of user {i}/3000")

    with open(f"User_Details/{i}.json", "r") as fp:
        user_dict = json.load(fp)
        created_at = datetime.strptime(user_dict['created_at'], "%Y-%m-%d %H:%M:%S%z")
        delta = current_time - created_at
        duration = delta.days + (delta.seconds / 86400)
        likes = int(user_dict['favourites_count'])
        duration_likes.append([duration, likes, (30*likes)/duration])

with open("User_Analysis/duration_likes_per_month.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(duration_likes)

print("Attributed Successfully Saved...")
