from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import csv
from time import time
from statistics import mean

start_time = time()

analyzer = SentimentIntensityAnalyzer()
user_sentiments = []

for i in range(1, 3001):
    print(f"Analysing for User {i}/3000")
    with open(f"User_Tweets/{i}.csv", "r", newline='') as fp:
        reader = csv.reader(fp)
        contents = [x[2] for x in list(reader)]
    if len(contents) == 0:
        user_sentiments.append([0.5])
        continue
    '''
    sentence = ' '.join(contents)
    vs = analyzer.polarity_scores(sentence)
    user_sentiments.append([0.5 + 0.5*(vs['pos'] - vs['neg'])])
    '''
    sentiments = []
    for sentence in contents:
        vs = analyzer.polarity_scores(sentence)
        score = vs['pos'] - vs['neg']
        if score != 0:
            sentiments.append(0.5 + 0.5*score)  # we are not appending 100% neutral sentiments
    if len(sentiments) != 0:
        user_sentiments.append([mean(sentiments)])
    else:
        user_sentiments.append([0.5])

with open("User_Analysis/VADER_Sentiment.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(user_sentiments)

print("Time_taken:", time()-start_time)
