from scipy import stats
import statistics
import csv
import matplotlib.pyplot as plt

test_index = 13
x_label = 'Median house price at User Location'

with open("Linear_Regression/VADER_Sentiment.csv", "r") as fp:
    reader = csv.reader(fp)
    output = [float(x[0]) for x in list(reader)]

values = []
with open("Linear_Regression/User_Attributes.csv", "r", newline='') as fp:
    reader = csv.reader(fp)
    headers = next(reader)
    for x in list(reader):
        if x[test_index] == '':
            values.append(0.0)
        else:
            values.append(float(x[test_index]))

# Scatter Plot
fig, ax = plt.subplots()
plt.scatter(values, output, alpha=0.95)

plt.xlabel(x_label)
plt.ylabel('Sentiment Score')
plt.show()
