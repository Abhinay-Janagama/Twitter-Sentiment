import pandas as pd
from collections import Counter
# Load your dataset (already cleaned and labeled)
df = pd.read_csv('D:\\Public Sentiment on AI and ChatGPT\\dataset\\final_sentiment_output.csv')
# Combine all cleaned tweets
all_text = ' '.join(df['Cleaned_Tweet'].dropna())
# Split into words
all_words = all_text.split()
# Count word frequency
word_freq = Counter(all_words)
# Convert to DataFrame
word_df = pd.DataFrame(word_freq.items(), columns=['Word', 'Frequency'])
# Sort by most frequent
word_df = word_df.sort_values(by='Frequency', ascending=False)

# Save to CSV
word_df.to_csv('D:\\Public Sentiment on AI and ChatGPT\\dataset\\top_words.csv', index=False)

print("Top words saved successfully!")
