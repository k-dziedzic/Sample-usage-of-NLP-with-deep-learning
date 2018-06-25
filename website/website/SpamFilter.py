import pickle
from nltk import word_tokenize
import os

def createDctionary(words):
    dictionary = dict([(word, True) for word in words])
    return dictionary

def spamFilter(message):
    words = word_tokenize(message)
    features = createDctionary(words)

    pwd = os.path.dirname(__file__)
    model = pwd + '/NB_classifier.pkl'

    with open(model, 'rb') as file:
        classifier = pickle.load(file)

    if classifier.classify(features)=="spam":
        return "SPAM"
    else:
        return "POŻĄDANA WIADOMOŚĆ"
