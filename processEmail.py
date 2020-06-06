import numpy as np
import pandas as pd


def process_email(email_contents):
    word_indices = []

    # set up vocabList, map word stem to index
    f = open('vocab.txt', "r")
    contents = f.read()
    str = contents.split()
    vocabList = {}

    for i in np.arange(0, len(str), 2):
        vocabList[str[i]] = str[i + 1]

    # preprocess email
    email_contents = email_contents.lower()
    







    return word_indices





if __name__ == '__main__':
    process_email('hi')
