import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import dateparser

# LangChain imports
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_community.llms import CTransformers


llm = CTransformers(
    model_file="./models/mistral-7b-instruct-v0.2.Q4_K_M.gguf",  # local GGUF file
    max_new_tokens=256,
    temperature=0.7
)


# ================================
# Load dataset
# ================================
df = pd.read_csv("reviews.csv")

# Convert Unix timestamp → date
df["Date"] = pd.to_datetime(df["Time"], unit="s").dt.date

# Map score → sentiment
def map_sentiment(score):
    if score < 3:
        return "negative"
    elif score == 3:
        return "neutral"
    else:
        return "positive"

df["Sentiment"] = df["Score"].apply(map_sentiment)

# ================================
# Agent 1 – Feedback Response
# ================================
sentiment_prompt = ChatPromptTemplate.from_template(
    "Analyze the sentiment of this customer review as positive, negative, or neutral: {text}"
)
sentiment_chain = (
    {"text": RunnablePassthrough()}
    | sentiment_prompt
    | llm
    | StrOutputParser()
)

reply_prompt = ChatPromptTemplate.from_template(
    "Generate a short, polite, context-aware reply to this {sentiment} customer review: {text}"
)
reply_chain = (
    {"sentiment": RunnablePassthrough(), "text": RunnablePassthrough()}
    | reply_prompt
    | llm
    | StrOutputParser()
)

def feedback_response_agent(review_text):
    sentiment = sentiment_chain.invoke(review_text).strip().lower()
    reply = reply_chain.invoke({"sentiment": sentiment, "text": review_text})
    return {"sentiment": sentiment, "reply": reply}

# ================================
# Agent 2 – Sentiment Visualization
# ================================
def parse_date_range(prompt):
    parts = prompt.lower().split(" to ")
    if len(parts) == 2:
        start = dateparser.parse(parts[0])
        end = dateparser.parse(parts[1])
    elif "last" in prompt:
        days = int(prompt.split("last ")[1].split(" day")[0])
        end = datetime.now().date()
        start = end - pd.Timedelta(days=days - 1)
    else:
        raise ValueError("Invalid date range. Use 'last X days' or 'start to end'.")
    return start.date(), end.date()

def sentiment_visualization_agent(date_prompt):
    start_date, end_date = parse_date_range(date_prompt)
    filtered_df = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]
    sentiment_counts = filtered_df.groupby(["Date", "Sentiment"]).size().unstack(fill_value=0)
    all_dates = pd.date_range(start=start_date, end=end_date).date
    sentiment_counts = sentiment_counts.reindex(all_dates, fill_value=0)

    plt.figure(figsize=(10, 6))
    sns.lineplot(data=sentiment_counts, markers=True)
    plt.title(f"Sentiment Trends from {start_date} to {end_date}")
    plt.xlabel("Date")
    plt.ylabel("Number of Reviews")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plot_path = "sentiment_plot.png"
    plt.savefig(plot_path)
    plt.close()
    return plot_path

# ================================
# Main
# ================================
if __name__ == "__main__":
    # Test Agent 1
    sample_review = "The food was great, but service was slow."
    response = feedback_response_agent(sample_review)
    print("Agent 1 Response:")
    print(f"Sentiment: {response['sentiment']}")
    print(f"Reply: {response['reply']}")

    # Test Agent 2
    plot = sentiment_visualization_agent("2012-01-01 to 2012-01-07")
    print(f"Agent 2 Plot saved to: {plot}")
