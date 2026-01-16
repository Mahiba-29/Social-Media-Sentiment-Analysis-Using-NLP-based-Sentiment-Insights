import requests
import json

headers = {"User-Agent": "sentiment-analysis-project"}

url = "https://www.reddit.com/r/technology.json?limit=150"
response = requests.get(url, headers=headers)

posts = []

for post in response.json()["data"]["children"]:
    data = post["data"]
    posts.append({
        "text": data["title"],
        "created_at": data["created_utc"],
        "source": "Reddit JSON"
    })

with open("data/raw_posts.json", "w") as f:
    json.dump(posts, f, indent=4)

print(" Data collected using Reddit public JSON")
