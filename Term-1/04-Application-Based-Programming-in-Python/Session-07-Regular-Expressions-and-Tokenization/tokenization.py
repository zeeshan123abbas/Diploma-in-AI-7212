# tokenization.py
# Tokenization = splitting text into small pieces (tokens) for NLP
import re
from collections import Counter

review = "The food was GREAT!!! Delivery took 45 mins, but the staff was polite. Great value."

# Step 1: simple split on spaces (punctuation stays attached)
print("split()        :", review.split())

# Step 2: word tokens with regex (\w+ keeps letters and digits)
words = re.findall(r"\w+", review.lower())
print("word tokens    :", words)

# Step 3: keep punctuation as separate tokens
tokens = re.findall(r"\w+|[^\w\s]", review)
print("with punct.    :", tokens)

# Step 4: sentence tokenization: split after . ! or ? followed by space
sentences = re.split(r"(?<=[.!?])\s+", review)
print("sentences      :", sentences)

# Step 5: remove stop words (very common words with little meaning)
stop_words = {"the", "was", "but", "a", "and", "took"}
clean = [w for w in words if w not in stop_words and not w.isdigit()]
print("clean tokens   :", clean)

# Step 6: count word frequency
print("most common    :", Counter(clean).most_common(3))
