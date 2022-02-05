import re
import csv
import json
from time import time

start_time = time()


# Only the word pray is used since, other words are often part of somme song or movie name
p1 = r'\bpray(ing)?\b'
pd_select = r'\b(god|jesus|pray)\b'
pd_reject = r'\b(atheist|no god)\b'

'''
text = "Lets pray for the affected people"

if re.search(p1, text, re.I):
    print("MATCH")
else:
    print("NOT_MATCH")
'''

religious_status = []

for i in range(1, 3001):
    print(f"Detecting religiousness in user {i}/3000")

    with open(f"User_Details/{i}.json", "r") as fp:
        user_dict = json.load(fp)
        description = user_dict['description']

    if re.search(pd_select, description, re.I):
        religious_status.append([1])
        # print("DescS:", re.search(pd_select, description, re.I))
        continue
    if re.search(pd_reject, description, re.I):
        religious_status.append([0])
        # print("DescR:", re.search(pd_reject, description, re.I))
        continue

    not_religious = True

    with open(f"User_Tweets/{i}.csv", "r", newline='') as fp:
        reader = csv.reader(fp)
        tweets = [x[2] for x in list(reader)]
        for tweet in tweets:
            if re.search(p1, tweet, re.I):
                religious_status.append([1])
                # print(re.search(p1, tweet, re.I))
                # print(tweet)
                not_religious = False
                break
    if not_religious:
        religious_status.append([0])

with open("User_Analysis/Religious_Status.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(religious_status)

num_religious = sum([x[0] for x in religious_status])
print(f"{num_religious} users are religious & {len(religious_status)-num_religious} users are not religious")
print("Time_Taken:", time()-start_time)
