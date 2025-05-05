import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def main():
    # Define the text paragraph
    text = """
            Hello all to python programming academy. Python programming academy is nice platform to learn new programming skills. It is difficult
            to get enrolled in this Academy.
"""
    text = text.translate(str.maketrans("", "", string.punctuation))

    sentences = sent_tokenize(text)

    words = [word.lower() for sentence in sentences for word in word_tokenize(sentence)]

    stop = set(stopwords.words("english"))
    filtered = [word for word in words if word.casefold not in stop]

    print("\nStop Words : \n", filtered)

    frequency = nltk.FreqDist(filtered)

    frequency.plot(25)
    plt.show()

    cloud = WordCloud(stopwords = stop).generate(text)
    plt.imshow(cloud)
    plt.show()
    
if __name__ == "__main__":
    main()
