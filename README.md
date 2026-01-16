# Social-Media-Sentiment-Analysis-Using-NLP-based-Sentiment-Insights
This project focuses on analyzing public sentiment from Reddit technology-related posts using Natural Language Processing (NLP) techniques and presenting the insights through an interactive Streamlit dashboard. The goal is to understand how users feel about technology topics by classifying posts as Positive, Negative, or Neutral, and visualizing these insights in a clean and professional interface.


**Social Media Sentiment Analysis System Architecture :**
<img width="800" height="600" alt="image" src="https://github.com/user-attachments/assets/d8e5a297-50d8-4c5c-bcb9-b7e5e8aeb710" />

**Objectives :**
- To collect and analyze text data from social media posts
- To perform sentiment analysis using NLP methods
- To compute polarity scores indicating emotional intensity
- To present insights visually through an interactive dashboard
- To enable non-technical users to easily interpret sentiment trends


**Commands to run :**

  pip install requests textblob pymongo matplotlib
  
  python scripts/reddit_fetch.py
  
  python scripts/clean_text.py
  
  python scripts/sentiment_analysis.py
  
  python scripts/mongo_store.py
  
  pip install streamlit matplotlib pandas wordcloud
  
  streamlit run scripts/dashboard.py


