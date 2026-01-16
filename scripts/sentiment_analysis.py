import json
from textblob import TextBlob

with open("data/clean_posts.json") as f:
    posts = json.load(f)

results = []

for post in posts:
    polarity = TextBlob(post["text"]).sentiment.polarity

    sentiment = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"

    results.append({
        "text": post["text"],
        "sentiment": sentiment,
        "polarity": polarity,
        "source": post["source"]
    })

with open("data/sentiment_results.json", "w") as f:
    json.dump(results, f, indent=4)

print("Sentiment analysis completed")
