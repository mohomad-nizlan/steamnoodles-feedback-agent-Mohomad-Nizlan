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
3. Download the local model:
   - Model: `mistral-7b-instruct-v0.2.Q4_K_M.gguf`  
   - Place it in the `models` folder:
    ```
    Nizlan_SteamNoodles/
    ├─ models/
    │  └─ mistral-7b-instruct-v0.2.Q4_K_M.gguf
    ```
4. Download the dataset:
   - Amazon Fine Food Reviews from [Kaggle](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews)
   - Place `reviews.csv` in the root folder:
    ```
    Nizlan_SteamNoodles/
    ├─ reviews.csv
    ```

## File Structure
<pre>
    Nizlan_SteamNoodles/
├─ agents.py # Main Python script to run agents
├─ models/
│ └─ mistral-7b-instruct-v0.2.Q4_K_M.gguf # Local LLM
├─ reviews.csv # Kaggle dataset
├─ README.md # Project instructions
</pre>

## How to Run / Test
Run the script:

```bash
python agents.py
```

## Usage Examples

### Agent 1 – Feedback Response
**Input Example:**  
"The food was great, but service was slow."

**Expected Output:**  
- Sentiment: neutral  
- Reply: Thank you for your feedback! We're glad you enjoyed the food and will work on improving our service.

### Agent 2 – Sentiment Visualization
**Input Example:**  
"2012-01-01 to 2012-01-07"

**Expected Output:**  
- Generates `sentiment_plot.png` showing daily sentiment trends.

### Notes / Tips
- Ensure the `models` folder contains the downloaded GGUF model.
- Ensure `reviews.csv` is in the project root.
- No OpenAI API key is required; everything runs locally.




