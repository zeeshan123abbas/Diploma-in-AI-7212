# pipeline_basics.py
# The first three stages of an NLP pipeline using ONLY plain Python.
# Stage 1: tokenization  Stage 2: normalization  Stage 3: stop word removal
# Command:  python pipeline_basics.py

import re

text = "The new Metro bus in Karachi is FAST! I love the new Metro bus."

# Stage 1: Tokenization -> split the text into words (tokens)
tokens = re.findall(r"[A-Za-z]+", text)   # keep letters only, drop "!" and "."
print("1. Tokens:          ", tokens)

# Stage 2: Normalization -> make every token lowercase
lower_tokens = [word.lower() for word in tokens]
print("2. Lowercase tokens:", lower_tokens)

# Stage 3: Stop word removal -> remove very common words that carry little meaning
stop_words = {"the", "is", "in", "a", "an", "i", "and", "of", "to"}
content_words = [word for word in lower_tokens if word not in stop_words]
print("3. Content words:   ", content_words)

# Bonus: count how often each content word appears
counts = {}
for word in content_words:
    counts[word] = counts.get(word, 0) + 1
print("Word counts:        ", counts)
