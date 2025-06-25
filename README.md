Twitter-Sentiment
Public sentiment on AI and ChatGpt
# Twitter Sentiment Analysis on AI and ChatGPT

This project analyzes public sentiment on AI and ChatGPT using Twitter data. It uses text preprocessing, VADER sentiment analysis, and various visualizations to explore how people feel about these technologies.
Aslo This repository  contains a Power BI dashboard that visualizes sentiment analysis results from Twitter data, providing insight into public opinion across tweets.
## 🔍 Overview
The project includes:
- **Text cleaning and preprocessing**
- **Sentiment classification (Positive, Negative, Neutral) using VADER**
- **Visualizations**:
  - Pie chart of sentiment distribution
  - Line chart of sentiment trends over time
  - Word cloud of common terms
- **Frequency analysis**:
  - Top frequent words overall
  - Top words by sentiment category

## 📁 Files

| File | Description |
|------|-------------|
| `Text Preprocessing.py` | Cleans the raw tweet data |
| `Sentiment Analysis.py` | Performs sentiment analysis using VADER |
| `Visualize Sentiment Trends.py` | Generates visualizations (pie chart, trend line, word cloud) |
| `word frequency.py` | Counts most frequent words in tweets |
| `word_by_sentiment.py` | Identifies top words per sentiment category |
| `final_sentiment_output.csv` | Cleaned tweets with sentiment labels |
| `sentiment_pie_chart.png` | Pie chart of sentiment distribution |
| `sentiment_trend_line.png` | Trend line of sentiment over time |
| `wordcloud.png` | Word cloud of common words |

## 📊 Sample Outputs

### Sentiment Distribution
![Pie Chart](sentiment_pie_chart.png)

### Sentiment Over Time
![Trend Line](sentiment_trend_line.png)

### Common Words
![Word Cloud](wordcloud.png)

## 🛠 Tools & Libraries
- Python
- Pandas
- Matplotlib, Seaborn
- NLTK
- VADER Sentiment Analyzer
- WordCloud

## 📂 Data
- Ensure your dataset (`sample_chatgpt_ai_tweets.csv`) is present in the appropriate directory.
- Preprocessed and final output files will be saved in CSV format.

## How to Run
1. Run `Text Preprocessing.py` to clean the tweets.
2. Run `Sentiment Analysis.py` to classify sentiment.
3. Run the visualization and word frequency scripts for insights and outputs.

---
# Twitter Sentiment Analysis Dashboard
This Power BI report helps you:

- Visualize sentiment distribution: Positive, Neutral, Negative
- Monitor tweet volume over time
- Explore commonly used hashtags and keywords
- Analyze user-based sentiment trends
- Interact with dynamic filters and visuals
- The page2 contain Most frequently used word in Tweets about AI and ChatGpt

## 🧰 Requirements

To open and interact with the report, you'll need:

- [Power BI Desktop](https://powerbi.microsoft.com/desktop/)

Open Twitter Sentiment.pbix using Power BI Desktop.

Explore the visuals and filter options.
