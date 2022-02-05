from keras.models import Sequential, load_model
from keras.layers import Dense
import csv
import numpy as np
import os

LOAD_MODEL = False

with open("Linear_Regression/Normalized_Attributes.csv", "r", newline='') as fp:
    reader = csv.reader(fp)
    headings = next(reader)
    dataset = np.array(list(reader), dtype=np.float)

with open("Linear_Regression/VADER_Sentiment.csv", "r", newline='') as fp:
    reader = csv.reader(fp)
    outputs = np.array([x[0] for x in list(reader)])

if os.path.isfile("Linear_Regression/model/regression_full.h5") and LOAD_MODEL:
    model = load_model("Linear_Regression/model/regression_full.h5")
else:
    model = Sequential()
    model.add(Dense(1, input_dim = 33, activation='linear'))

    model.compile(loss='mse', optimizer='rmsprop', metrics=['mse'])
model.fit(x=dataset, y=outputs, epochs=40, verbose=1)

model.save("Linear_Regression/model/regression_full.h5")

model.summary()
weights = model.get_weights()

weights_list = []

for i, w in enumerate(weights[0]):
    print(f'{i+1}) {headings[i]} : {w[0]}')
    weights_list.append([headings[i], w[0]])
print(f'34) BIAS: {weights[1][0]}\n')
weights_list.append(['BIAS', weights[1][0]])

with open("Linear_Regression/Full_weights.csv", "w", newline='') as fp:
    writer = csv.writer(fp)
    writer.writerows(weights_list)

print(len(weights), len(weights[0]), len(weights[1]))
print(model.predict(dataset[:10]))
print(outputs[:10])

print(np.sum(dataset[0]*np.array([x[0] for x in weights[0]]))+weights[1][0], model.predict(np.array([dataset[0]])))
