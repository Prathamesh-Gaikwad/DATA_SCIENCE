import string
import re


text = """
        Hello, #world123! This is a sample text paragraph. It contains
        special characters and 5 digits.
"""

#new = re.sub(r'[^a-zA-Z]', '', text)

text = text.translate(str.maketrans("", "", string.punctuation))

print("\nSpecial Charcter Removed Text : \n", text)

