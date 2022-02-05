from scipy import stats
import statistics
import csv
import matplotlib.pyplot as plt

test_index = 15
g1_name = 'Users who are NOT Religious'
g2_name = 'Users who are Religious'
opacity = 0.75
g1_first = False
binary_attribute = True

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


if binary_attribute:
    g1, g2 = [], []
    for i, x in enumerate(values):
        if round(x) == 0:
            g1.append(output[i])
        else:
            g2.append(output[i])
    print(f'The number of users with "1" for {headers[test_index]} is {len(g2)} & "0" is {len(g1)}')
else:
    median = statistics.median(values)
    print(f'The Median of {headers[test_index]} is {median}.')

    g1, g2 = [], []
    for i, x in enumerate(values):
        if x <= median:
            g1.append(output[i])
        else:
            g2.append(output[i])

print("Ttest output is:", stats.ttest_ind(g1, g2))
# t value - size of the difference relative to the variation in your sample data (more is better)
#               = (variance between groups / variance within groups) = should be more then 1
# p value - the probability that the pattern of data in sample could be produced by random data (better if less than 5%)

# Histogram Plot
fig, ax = plt.subplots()
if g1_first:
    plt.hist(g1, alpha=opacity, label=g1_name)
    plt.hist(g2, alpha=opacity, label=g2_name)
else:
    plt.hist(g2, alpha=opacity, label=g2_name)
    plt.hist(g1, alpha=opacity, label=g1_name)
ax.legend(loc = 'best')

plt.xlabel('Sentiment Score')
plt.ylabel('Frequency')
plt.show()
