import numpy as np
import pandas as pd
import re

from nltk.stem import PorterStemmer


# set up vocabList, map word stem to index
f = open('vocab.txt', "r")
contents = f.read()
str = contents.split()
vocabList = {}

for i in np.arange(0, len(str), 2):
    vocabList[str[i + 1]] = str[i]

def process_email(email_contents):
    word_indices = []

    # preprocess email
    email_contents = email_contents.lower()

    # remove HTML
    email_contents = re.sub('html', ' ', email_contents)

    # normalize URLS
    email_contents = re.sub('(http|https)://[^\s]*', 'httpaddr', email_contents)

    # normalize emails
    email_contents = re.sub('[^\s]+@[^\s]+', 'emailaddr', email_contents)

    # normalize numbers
    email_contents = re.sub('[0-9]+', 'number', email_contents)

    # normalize dollars
    email_contents = re.sub('[$]+', 'dollar', email_contents)

    # remove non-words
    email_contents = re.sub('@$/#.-:&*+=[]?!(){},''">_<;%', '', email_contents)
    email_contents = regexprep('[^a-zA-Z0-9]', '', email_contents)

    # stemming words
    ps = PorterStemmer()
    words = email_contents.split()
    # words = [ps.stem(w) for w in words]

    for w in words:
        w = ps.stem(w)
        if w in vocabList:
            word_indices.append(vocabList[w])

    return word_indices


def email_features(word_indices):
    features = np.zeros(len(vocabList))

    for i in range(len(word_indices)):
        features[word_indices[i] - 1] = 1
    return features
