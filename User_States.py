import csv
import json
from uszipcode import SearchEngine
from time import time

start_time = time()

search = SearchEngine()
user_states = []
states_dict = {}

for i in range(1, 3001):
    print(f"Finding State of user {i}/3000")

    with open(f"User_Details/{i}.json", "r") as fp:
        user_dict = json.load(fp)
        zipcode = user_dict['zipcode']
        z_code = search.by_zipcode(zipcode)
        user_states.append([z_code.state])
        if z_code.state in states_dict:
            states_dict[z_code.state] += 1
        else:
            states_dict[z_code.state] = 1

with open("User_Analysis/User_States.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(user_states)

with open("User_Analysis/User_States.json", "w") as fp:
        json.dump(states_dict, fp)

print("Time_Taken:", time()-start_time)
