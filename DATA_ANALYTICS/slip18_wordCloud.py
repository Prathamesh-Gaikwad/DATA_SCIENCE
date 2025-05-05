import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def main():
    # Define the text paragraph
    text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed tristique ante et velit vestibulum, vel pharetra orci acculis. Nullam mattis risus quis augue tincidunt rhoncus. Morbi varius, arcu vitaes celerisque laoreet, magna est imperdiet quam, sit amet ultrices lectus justo id enim. Sed dictum suscipit commodo. Sed maximus consequat risus, nec pharetra nibh interdum quis. Etiameget quam vel augue dictum dignissim sit amet nec elit. Nunc at sapien dolor. Nulla vitae iaculis lorem. Suspendisse potenti. Sed non ante turpis. Morbi consectetur, arcu vestibulum suscipit, mauris eros convallis nibh, nec feugiat orci enim sit amet enim. Aliquam erat volutpat. Etiam vel nisi id neque viverra dapibus non non lectus."""

    # Tokenize the paragraph to extract words and sentences
    words = word_tokenize(text.lower())
    sentences = sent_tokenize(text)

    # Remove stopwords from the extracted words
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.casefold() not in stop_words]

    # Calculate the word frequency distribution
    word_freq = FreqDist(filtered_words)

    # Plot the word frequency distribution
    word_freq.plot(25)
    plt.show()

    # Plot the word cloud of the text
    cloud = WordCloud(stopwords=stop_words).generate(text)
    plt.imshow(cloud)
    plt.show()

if __name__ == "__main__":
    main()
