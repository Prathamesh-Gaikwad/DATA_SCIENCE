import string
import nltk
from heapq import nlargest
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

def main():
    text = "Hi I'm @#$^&^*& Prathamesh. Learning ^&(*)(* Language Processing. Interesting to see Python's Power."

    text = text.translate(str.maketrans("", "", string.punctuation))

    sentences = sent_tokenize(text)

    words = [word.lower() for sentence in sentences for word in word_tokenize(sentence)]

    frequency = nltk.FreqDist(words)

    scores = {}

    for sentence in sentences:
        words = word_tokenize(sentence)
        score = sum(frequency.get(word, 0) for word in words)
        scores[sentence] = score

    summary = nlargest(3, scores, key = scores.get)

    print("\nSummary : \n", summary)

if __name__ == "__main__":
    main()
