import os
import pyensae
from nltk.classify import NaiveBayesClassifier
from nltk.tokenize import word_tokenize
import nltk.classify.util
import pickle

# download Enron-Spam datasets
pyensae.download_data("enron1.tar.gz", url="http://www.aueb.gr/users/ion/data/enron-spam/preprocessed/",
                      whereTo="website/dataSources/enron")
pyensae.download_data("enron2.tar.gz", url="http://www.aueb.gr/users/ion/data/enron-spam/preprocessed/",
                      whereTo="website/dataSources/enron")
pyensae.download_data("enron3.tar.gz", url="http://www.aueb.gr/users/ion/data/enron-spam/preprocessed/",
                      whereTo="website/dataSources/enron")
pyensae.download_data("enron4.tar.gz", url="http://www.aueb.gr/users/ion/data/enron-spam/preprocessed/",
                      whereTo="website/dataSources/enron")
pyensae.download_data("enron5.tar.gz", url="http://www.aueb.gr/users/ion/data/enron-spam/preprocessed/",
                      whereTo="website/dataSources/enron")
pyensae.download_data("enron6.tar.gz", url="http://www.aueb.gr/users/ion/data/enron-spam/preprocessed/",
                      whereTo="website/dataSources/enron")

pathToDatasets = "website/dataSources/enron"


# get word, and return dictionary
def createDctionary(words):
    dictionary = dict([(word, True) for word in words])
    return dictionary


ham_tab = []
spam_tab = []

# Read files, and split words in string with word_tokenize() and create dictionary
for folders, subfolders, files in os.walk(pathToDatasets):
    if os.path.split(folders)[1] == 'ham':
        for file in files:
            with open(os.path.join(folders, file), encoding="latin-1") as nextFile:
                data = nextFile.read()
                # break string into words with nltk library
                words = word_tokenize(data)
                ham_tab.append((createDctionary(words), "ham"))

    if os.path.split(folders)[1] == 'spam':
        for file in files:
            try:
                with open(os.path.join(folders, file), encoding="latin-1") as nextFile:
                    data = nextFile.read()
                    words = word_tokenize(data)
                    spam_tab.append((createDctionary(words), "spam"))
            except:
                print(file)

# split data into 80% train data and 20% test data
combined_tab = ham_tab + spam_tab

training_part = int(len(combined_tab) * .8)
training_set = combined_tab[:training_part]

test_set = combined_tab[training_part:]

# Create NB classifier
classifier = NaiveBayesClassifier.train(training_set)

# print(nltk.classify.util.accuracy(classifier, test_set))

# save to file
with open('website/website/NB_classifier.pkl', 'wb') as file:
    pickle.dump(classifier, file)
