import json
import re

with open("data/raw_posts.json") as f:
    posts = json.load(f)

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-z\s]", "", text)
    return text

cleaned = []

for post in posts:
    cleaned.append({
        "text": clean_text(post["text"]),
        "created_at": post["created_at"],
        "source": post["source"]
    })

with open("data/clean_posts.json", "w") as f:
    json.dump(cleaned, f, indent=4)

print("Text cleaned successfully")
