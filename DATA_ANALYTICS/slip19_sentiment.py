import pandas as pd
from textblob import TextBlob
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

def main():
    # Load the dataset
    df = pd.read_csv('movie_review.csv')

    # Add a column for sentiment analysis using TextBlob
    df['Sentiment'] = df['Review'].apply(lambda x: TextBlob(x).sentiment.polarity)

    # Create a new dataframe for positive reviews only
    pos_df = df[df['Sentiment'] > 0.2]

    # Create a word cloud for positive reviews
    wordcloud = WordCloud(width=800, height=800, background_color='white', stopwords=STOPWORDS, min_font_size=10).generate(' '.join(pos_df['Review']))

    # Plot the word cloud
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.show()

if __name__ == "__main__":
    main()

