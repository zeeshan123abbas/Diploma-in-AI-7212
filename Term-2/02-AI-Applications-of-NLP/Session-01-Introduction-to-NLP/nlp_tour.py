# nlp_tour.py
# A quick tour of classic NLP tasks with NLTK.
# First run setup_nltk.py once.   Command:  python nlp_tour.py

import nltk
from nltk.stem import WordNetLemmatizer

sentence = "Ayesha visited Lahore in March and bought three books."

# 1) Tokenization: split the sentence into words
words = nltk.word_tokenize(sentence)
print("Tokens:", words)

# 2) Part-of-speech tagging: label each word as noun, verb, etc.
tags = nltk.pos_tag(words)
print("POS tags:", tags)          # NNP = proper noun, VBD = past-tense verb ...

# 3) Lemmatization: reduce a word to its dictionary form
lemmatizer = WordNetLemmatizer()
print("Lemma of 'books':", lemmatizer.lemmatize("books"))            # book
print("Lemma of 'bought':", lemmatizer.lemmatize("bought", pos="v"))  # buy

# 4) Named Entity Recognition: find names of people, places ...
tree = nltk.ne_chunk(tags)
for chunk in tree:
    if hasattr(chunk, "label"):                         # entities are sub-trees
        entity = " ".join(word for word, tag in chunk)
        print("Entity:", entity, "->", chunk.label())
