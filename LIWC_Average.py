import csv
import numpy as np
from time import time

start_time = time()

# Note that the 1st line of LIWC file is just headings
LIWC_lines = 0
LIWC_user_results = []

with open("Users_Count.csv", "r", newline='') as f:
    reader = csv.reader(f)
    users_count = list(reader)
users_count = [int(x[3]) for x in users_count]
# users_count = users_count[:20]

with open("LIWC_Results/LIWC2015_Results.csv", "r", newline='') as f:
    reader = csv.reader(f)
    LIWC_user_results.append(list(next(reader))[1:])    # To add 1st line with headings separately
    curr_user = 0
    next_goal = users_count[curr_user] - 1
    curr_user_attr = []
    for i, line in enumerate(reader):
        LIWC_lines += 1
        curr_user_attr.append(line[1:])
        if i == next_goal:
            curr_user_attr = np.array(curr_user_attr, dtype=np.float)
            LIWC_user_results.append(np.mean(curr_user_attr, axis=0))
            print(f"Metrics of User {curr_user+1} averaged")
            curr_user_attr = []
            curr_user += 1
            if curr_user < len(users_count):
                if users_count[curr_user] == 0:
                    curr_user += 1
                    LIWC_user_results.append(np.zeros(93, dtype=np.float))
                    print(f"Metrics of User {curr_user+1} averaged (User skipped - no tweets present)")
                next_goal += users_count[curr_user]
            # else:
            #    break


with open("LIWC_Results/LIWC_User_Results.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(LIWC_user_results)

print("Users tweet count:", sum(users_count))
print("LIWC lines:", LIWC_lines)
print("Time Taken:", time()-start_time)
