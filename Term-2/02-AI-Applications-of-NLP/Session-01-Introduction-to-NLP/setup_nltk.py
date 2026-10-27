# setup_nltk.py
# Run this file ONCE on your computer (internet needed).
# It downloads the small data packages that NLTK uses in this module.
# Command:  python setup_nltk.py

import nltk

packages = [
    "punkt_tab",                       # sentence and word tokenizer
    "stopwords",                       # lists of common words (the, is, a ...)
    "wordnet",                         # English dictionary used by the lemmatizer
    "averaged_perceptron_tagger_eng",  # part-of-speech tagger
    "maxent_ne_chunker_tab",           # named entity chunker
    "words",                           # word list needed by the NE chunker
    "vader_lexicon",                   # sentiment word scores
]

for name in packages:
    ok = nltk.download(name, quiet=True)
    print(f"{name:32} ->", "ready" if ok else "FAILED (check internet)")
