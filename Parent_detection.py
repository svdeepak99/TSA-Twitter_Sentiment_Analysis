import re
import csv
import json
from time import time

start_time = time()

# The commented lines are more accurate, but it is giving too many parents
# p1 = r'(my|our|i have)[^.]*[^.\da-z]([1-9]|1[0-9]|20)[ -]?((years?|months?)[ -]?old|yo)'
# p2 = r'(my|our|i have)[^.]*[^.\da-z](kids?|child(ren)?|sons?|daughters?)'  # Had to remove boy(s)&girl(s) due to phrasal context

p1 = r'(my|our) ([1-9]|1[0-9]|20)[ -]?((years?|months?)[ -]?old|yo)'
p2 = r'(my|our) (kids?|child(ren)?|sons?|daughters?)'  # Had to remove boy(s) & girl(s) due to phrasal context
pd_select = r'(parent|mother|father|mom|dad)'
pd_reject = r'(grandpa|grandfather|grandma|grandmother)'

'''
text = "I have a nice 3 year old"

if re.search(p1, text, re.I) or re.search(p2, text, re.I):
    print("MATCH")
else:
    print("NOT_MATCH")
'''

parent_status = []

for i in range(1, 3001):
    print(f"Detecting parenthood in user {i}/3000")

    with open(f"User_Details/{i}.json", "r") as fp:
        user_dict = json.load(fp)
        description = user_dict['description']

    if user_dict['age']['value'] < 15:
        parent_status.append([0])
        # print("Age only", user_dict['age']['value'])
        continue
    if re.search(pd_select, description, re.I):
        parent_status.append([1])
        # print("DescS:", re.search(pd_select, description, re.I))
        continue
    if re.search(pd_reject, description, re.I):
        parent_status.append([0])
        # print("DescR:", re.search(pd_reject, description, re.I))
        continue

    not_parent = True

    with open(f"User_Tweets/{i}.csv", "r", newline='') as fp:
        reader = csv.reader(fp)
        tweets = [x[2] for x in list(reader)]
        for tweet in tweets:
            if re.search(p1, tweet, re.I) or re.search(p2, tweet, re.I):
                parent_status.append([1])
                # print(re.search(p1, tweet, re.I), re.search(p2, tweet, re.I))
                not_parent = False
                break
    if not_parent:
        parent_status.append([0])

with open("User_Analysis/Parent_Status.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(parent_status)

num_parents = sum([x[0] for x in parent_status])
print(f"{num_parents} users are parents & {len(parent_status)-num_parents} users are not parents")
print("Time_Taken:", time()-start_time)
