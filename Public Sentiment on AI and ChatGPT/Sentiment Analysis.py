import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load the cleaned dataset
df = pd.read_csv('D:\\Public Sentiment on AI and ChatGPT\\dataset\\cleaned_chatgpt_ai_tweets.csv')

# Initialize VADER
analyzer = SentimentIntensityAnalyzer()

# Function to determine sentiment
def get_sentiment(text):
    score = analyzer.polarity_scores(text)['compound']
    if score >= 0.05:
        return 'Positive'
    elif score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Apply sentiment analysis
df['Sentiment'] = df['Cleaned_Tweet'].apply(get_sentiment)

# Show results
print(df[['Tweet', 'Cleaned_Tweet', 'Sentiment']].head())

# Optionally save the final output
df.to_csv('D:\\Public Sentiment on AI and ChatGPT\\dataset\\final_sentiment_output.csv', index=False)
