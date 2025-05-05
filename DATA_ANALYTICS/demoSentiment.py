import pandas as pd
from matplotlib.pyplot as plt
from textblob import TextBlob
from wordcloud import WordCloud

def main():
    df = pd.read_csv("Movie_Review.csv")

    df['Sentiment'] = df['Review'].apply(lambda x:TextBlob(x).sentiment.polarity)

    positive = df[df['Review'] > 0.2]

    cloud = WordCloud(stopwords = STOPWORDS).generate(' '.join(positive['Review']))

    plt.imshow(cloud)
    plt.show()

if __name__ "__main__" :
    main()
