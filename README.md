# SteamNoodles Feedback Agent –Mohomad Nizlan

## Your Details
- **Name:** Mohomad Nizlan
- **University:** University of Moratuwa
- **Year:** 2nd year

## Project Overview
This project implements **two AI agents** using LangChain and **local LLMs** via CTransformers:

- **Agent 1 – Feedback Response:** Analyzes sentiment (positive/negative/neutral) and generates polite replies.
- **Agent 2 – Sentiment Visualization:** Plots sentiment trends over a user-specified date range using line plots.

**Dataset:** Amazon Fine Food Reviews (Kaggle) mapped to sentiments.

## Setup Instructions
1. Clone this repository:
    ```bash
    git clone "https://github.com/mohomad-nizlan/steamnoodles-feedback-agent-Mohomad-Nizlan.git"
    cd Nizlan_SteamNoodles
    ```
2. Install required packages:
    ```bash
    pip install langchain langchain-community ctransformers pandas matplotlib seaborn dateparser
    ```
3. Place your local model file in a `models` folder:
    ```
    models/mistral-7b-instruct-v0.2.Q4_K_M.gguf
    ```
4. Download dataset from [Kaggle Amazon Fine Food Reviews](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews) and place `reviews.csv` in the project root.

## How to Run / Test
Run the script:

```bash
python agents.py
