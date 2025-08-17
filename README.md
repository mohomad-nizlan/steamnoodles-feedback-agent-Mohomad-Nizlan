# SteamNoodles Feedback Agent – Mohomad Nizlan

## Your Details
- **Name:** Mohomad Nizlan
- **University:** University of Moratuwa
- **Year:** 2nd year

## Project Overview
This project implements **two AI agents** using LangChain and OpenAI GPT:

- **Agent 1 – Feedback Response:** Analyzes sentiment (positive/negative/neutral) and generates polite replies.
- **Agent 2 – Sentiment Visualization:** Plots sentiment trends over a user-specified date range using line plots.

**Dataset:** Amazon Fine Food Reviews (Kaggle) mapped to sentiments.

## Setup Instructions
1. Clone this repository:
    ```bash
    git clone <repo-url>
    cd Nizlan_SteamNoodles
    ```
2. Install required packages:
    ```bash
    pip install langchain langchain-openai openai pandas matplotlib seaborn python-dotenv dateparser
    ```
3. Add a `.env` file in the project root with:
    ```text
    OPENAI_API_KEY=your_openai_api_key_here
    ```
4. Download dataset from [Kaggle Amazon Fine Food Reviews](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews) and place `reviews.csv` in the project root.

## How to Run / Test
Run the script:

```bash
python agents.py
