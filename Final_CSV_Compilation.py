import csv
import json
from time import time

# The following attributes will be combined in the final csv
'''
1) tweets - Tweets per month
2) followers
3) friends
4) listed
5) duration (in days)
6) likes (likes per month)
7) verified
8) age
9) gender
10) smile
11) population density
12) water level
13) income
14) home value
15) parent
16) religious
17) Average Words (LIWC WC)
18) Analytic
19) Confidence (Clout)
20) Authentic
21) Exclamation
22) negate
23) swear words
24) Self (i, me, our)
25) Group (we, us, our)
26) power	(people who show superiority/bully)
27) risk
28) home
29) work
30) money
31) sexual
32) Reasoning (cause)
33) Certainty
'''

start_time = time()

csv_attributes = [['Tweets', 'Followers', 'Friends', 'Listed', 'Duration', 'Likes', 'Verified', 'Age', 'Gender', 'Smile', 'Population Density', 'Water Level', 'Income', 'Home Value', 'Parent', 'Religious', 'Average Words', 'Analytic', 'Confidence', 'Authentic', 'Exclamation', 'Negate', 'Swear Words', 'Self(i)', 'Group(we)', 'Power', 'Risk', 'Home', 'Work', 'Money', 'Sexual', 'Reasoning', 'Certainty']]

with open("Users_Count.csv", "r", newline='') as fp:
    reader = csv.reader(fp)
    tweets_per_month = [x[5] for x in list(reader)]

duration = []
likes_per_month = []
with open("User_Analysis/duration_likes_per_month.csv", "r", newline='') as f:
    reader = csv.reader(f)
    for dur in list(reader):
        duration.append(dur[0])
        likes_per_month.append(dur[2])

with open("User_Analysis/Parent_Status.csv", "r", newline='') as fp:
    reader = csv.reader(fp)
    parent_status = [x[0] for x in list(reader)]

with open("User_Analysis/Religious_Status.csv", "r", newline='') as fp:
    reader = csv.reader(fp)
    religious_status = [x[0] for x in list(reader)]

with open("LIWC_Results/LIWC_User_Results.csv", "r", newline='') as fp:
    reader = csv.reader(fp)
    LIWC_attributes = [[x[0], x[1], x[2], x[3], x[87], x[22], x[76], x[11], x[12], x[59], x[61], x[71], x[69], x[72], x[54], x[42], x[45]] for x in list(reader)]

for i in range(1, 3001):
    print(f"Compiling attributes of user {i}/3000")

    with open(f"User_Details/{i}.json", "r") as fp:
        user_dict = json.load(fp)

    user_attributes = [
        tweets_per_month[i-1],
        user_dict['followers_count'],
        user_dict['friends_count'],
        user_dict['listed_count'],
        duration[i-1],
        likes_per_month[i-1],
        int(user_dict['verified']),
        user_dict['age']['value'],
        int(user_dict['gender']['value'] == "Male"),
        int(user_dict['smile']),
        user_dict['population_density'],
        user_dict['water_level'],
        user_dict['median_household_income'],
        user_dict['median_home_value'],
        parent_status[i-1],
        religious_status[i-1]
    ]

    csv_attributes.append(user_attributes + LIWC_attributes[i])


with open("Linear_Regression/User_Attributes.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(csv_attributes)

print("Attributed Compiled! Time Taken:", time()-start_time)
