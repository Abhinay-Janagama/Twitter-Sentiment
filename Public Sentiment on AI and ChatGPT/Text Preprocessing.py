import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Load the dataset
df = pd.read_csv('D:\\Public Sentiment on AI and ChatGPT\\dataset\\sample_chatgpt_ai_tweets.csv')  # Make sure this file is in the same folder as your script

# Clean the tweets
def clean_text(text):
    text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)  # Remove URLs
    text = re.sub(r'\@\w+|\#', '', text)  # Remove mentions and hashtags
    text = re.sub(r"[^a-zA-Z\s]", '', text)  # Remove punctuation
    text = text.lower()  # Lowercase
    text = " ".join(word for word in text.split() if word not in stop_words)  # Remove stopwords
    return text

df['Cleaned_Tweet'] = df['Tweet'].apply(clean_text)
print(df[['Tweet', 'Cleaned_Tweet']].head())
# Save cleaned data to CSV
df.to_csv('D:\\Public Sentiment on AI and ChatGPT\\dataset\\cleaned_chatgpt_ai_tweets.csv', index=False)

