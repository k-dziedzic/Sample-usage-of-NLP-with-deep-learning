import pickle
from nltk import word_tokenize
import os


def create_dctionary(words):
    dictionary = dict([(word, True) for word in words])
    return dictionary


def spam_filter(message):
    words = word_tokenize(message)
    features = create_dctionary(words)

    pwd = os.path.dirname(__file__)
    model = pwd + '/NB_classifier.pkl'

    with open(model, 'rb') as file:
        classifier = pickle.load(file)

    if classifier.classify(features) == "spam":
        return "SPAM"
    else:
        return "POŻĄDANA WIADOMOŚĆ"
