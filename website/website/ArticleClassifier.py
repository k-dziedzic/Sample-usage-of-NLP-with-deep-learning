import os

labelDict = {"__label__political": "Polityczny",
             "__label__sport": "Sportowy",
             "__label__technology": "Techniczny"}


def classify(text):
    pwd = os.path.dirname(__file__)
    filePath = pwd + '/text.txt'
    textFile = open(filePath, "w", encoding="utf8")
    textFile.write(text.replace('\n', ' '))
    textFile.close()
    model = pwd + '/articles.ftz'
    label = os.popen("fasttext predict "+model+" "+filePath).read()
    label = str(label).replace('\n', '')
    return labelDict[label]

