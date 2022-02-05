import csv
import numpy as np
from time import time

start_time = time()

with open("Linear_Regression/User_Attributes.csv", "r", newline='') as fp:
    reader = csv.reader(fp)
    headings = list(next(reader))
    data = np.array(list(reader))
    data[data == ''] = '0'
    data = np.array(data, dtype=np.float)

print("Finding Max Vector:")
max_vect = np.max(data, axis=0)
print("Dividing by Max Vector:")
normalized_data = data / max_vect

with open("Linear_Regression/Normalized_Attributes.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headings)
    writer.writerows(normalized_data)

print("Time Taken:", time()-start_time)
