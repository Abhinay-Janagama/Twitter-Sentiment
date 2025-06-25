import pandas as pd
from collections import Counter

#Step 1: Load your dataset
df = pd.read_csv('D:\\Public Sentiment on AI and ChatGPT\\dataset\\final_sentiment_output.csv')

#Step 2: Create list to hold word frequency by sentiment
word_tables = []

#Step 3: Loop through each sentiment and collect top 10 words
for sentiment in ['Positive', 'Negative', 'Neutral']:
    # Filter tweets by sentiment
    tweets = df[df['Sentiment'] == sentiment]['Cleaned_Tweet'].dropna()
    words = ' '.join(tweets).split()
    
    # Count most common words
    common = Counter(words).most_common(10)
    
    for word, count in common:
        word_tables.append({'Sentiment': sentiment, 'Word': word, 'Frequency': count})

#Step 4: Convert to DataFrame
word_sentiment_df = pd.DataFrame(word_tables)

#Step 5: Save to CSV
word_sentiment_df.to_csv('D:\\Public Sentiment on AI and ChatGPT\\dataset\\word_by_sentiment.csv', index=False)

print("Top words by sentiment saved successfully!")
