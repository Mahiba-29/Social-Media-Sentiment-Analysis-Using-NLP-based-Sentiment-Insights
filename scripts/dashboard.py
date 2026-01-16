import streamlit as st
import json
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

st.set_page_config(
    page_title="Social Media Sentiment Dashboard",
    layout="wide"
)

st.markdown("""
<div style="
    background: linear-gradient(90deg, #1e3a8a, #2563eb);
    padding: 2.5rem;
    border-radius: 16px;
    margin-bottom: 2.5rem;
">
    <h1 style="
        color: white;
        font-size: 36px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 0.3rem;
    ">
        Social Media Sentiment Analysis Dashboard using NLP-based Sentiment Insights
    </h1>

       Dataset from: Public Reddit Technology Posts
</div>
""", unsafe_allow_html=True)

st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont,
                 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
}

.block-container {
    padding-top: 1rem;
    padding-bottom: 2.5rem;
}

.kpi-card {
    background-color: #f9fafb;
    border-radius: 14px;
    padding: 1.6rem;
    border-left: 6px solid #2563eb;
}

.kpi-title {
    font-size: 14px;
    color: #6b7280;
    margin-bottom: 0.2rem;
}

.kpi-value {
    font-size: 30px;
    font-weight: 600;
    color: #111827;
}
</style>
""", unsafe_allow_html=True)


with open("data/sentiment_results.json") as f:
    data = json.load(f)

df = pd.DataFrame(data)
sentiment_counts = df["sentiment"].value_counts()

st.subheader("Sentiment Overview")

k1, k2, k3 = st.columns(3)

with k1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Positive</div>
        <div class="kpi-value">{sentiment_counts.get("Positive", 0)}</div>
    </div>
    """, unsafe_allow_html=True)

with k2:
    st.markdown(f"""
    <div class="kpi-card" style="border-left-color:#dc2626;">
        <div class="kpi-title">Negative</div>
        <div class="kpi-value">{sentiment_counts.get("Negative", 0)}</div>
    </div>
    """, unsafe_allow_html=True)

with k3:
    st.markdown(f"""
    <div class="kpi-card" style="border-left-color:#6b7280;">
        <div class="kpi-title">Neutral</div>
        <div class="kpi-value">{sentiment_counts.get("Neutral", 0)}</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

c1, c2 = st.columns(2)

with c1:
    st.subheader("Sentiment Distribution")
    st.bar_chart(sentiment_counts)

with c2:
    st.subheader("Sentiment Share")
    fig1, ax1 = plt.subplots()
    ax1.pie(
        sentiment_counts,
        labels=sentiment_counts.index,
        autopct="%1.1f%%",
        startangle=120,
        wedgeprops={"width": 0.45}
    )
    ax1.axis("equal")
    st.pyplot(fig1)

st.divider()

c3, c4 = st.columns(2)

with c3:
    st.subheader("Polarity Score Distribution")
    fig2, ax2 = plt.subplots()
    ax2.hist(df["polarity"], bins=20)
    ax2.set_xlabel("Polarity Score (-1 to +1)")
    ax2.set_ylabel("Number of Posts")
    st.pyplot(fig2)

with c4:
    st.subheader("Polarity by Sentiment")
    fig3, ax3 = plt.subplots()
    df.boxplot(column="polarity", by="sentiment", ax=ax3)
    plt.suptitle("")
    ax3.set_ylabel("Polarity Score")
    st.pyplot(fig3)

st.divider()

st.subheader("Discussion Keywords")
st.caption("Most frequent terms appearing in Reddit technology discussions")

text = " ".join(df["text"])

wordcloud = WordCloud(
    width=1000,
    height=420,
    background_color="white"
).generate(text)

st.image(wordcloud.to_image(), use_container_width=True)

with st.expander("View Analyzed Dataset"):
    st.dataframe(df, use_container_width=True)
