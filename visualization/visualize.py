import json
import matplotlib.pyplot as plt

with open("data/sentiment_results.json") as f:
    data = json.load(f)

counts = {"Positive": 0, "Negative": 0, "Neutral": 0}

for post in data:
    counts[post["sentiment"]] += 1

plt.bar(counts.keys(), counts.values())
plt.title("Sentiment Analysis of Reddit Technology Posts")
plt.show()
