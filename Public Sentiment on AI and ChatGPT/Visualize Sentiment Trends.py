import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load the sentiment-labeled dataset
df = pd.read_csv('D:\\Public Sentiment on AI and ChatGPT\\dataset\\final_sentiment_output.csv')

# Convert Date column to datetime (needed for trend plot)
df['Date'] = pd.to_datetime(df['Date'])

# --- PIE CHART ---
sentiment_counts = df['Sentiment'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=140,
        colors=['lightgreen', 'lightblue', 'salmon'])
plt.title('Sentiment Distribution')
plt.axis('equal')
plt.savefig('D:\\Public Sentiment on AI and ChatGPT\\images\\sentiment_pie_chart.png')  # Save image
plt.show()

# --- LINE PLOT (Trend over Time) ---
df_trend = df.groupby([df['Date'].dt.date, 'Sentiment']).size().unstack().fillna(0)
df_trend.plot(kind='line', figsize=(10, 5), marker='o')
plt.title('Sentiment Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Tweet Count')
plt.grid(True)
plt.tight_layout()
plt.savefig('D:\\Public Sentiment on AI and ChatGPT\\images\\sentiment_trend_line.png')  # Save image
plt.show()

# --- WORD CLOUD ---
all_words = ' '.join(df['Cleaned_Tweet'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_words)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Common Words in Tweets")
plt.savefig('D:\\Public Sentiment on AI and ChatGPT\\images\\wordcloud.png')  # Save image
plt.show()
