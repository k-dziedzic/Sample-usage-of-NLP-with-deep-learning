import os

labelDict = {"__label__political": "Polityczny",
             "__label__sport": "Sportowy",
             "__label__technology": "Techniczny",
             "other": "Inny"}


def classify(text):
    pwd = os.path.dirname(__file__)
    filePath = pwd + '/text.txt'
    textFile = open(filePath, "w", encoding="utf8")
    textFile.write(text.replace('\n', ' '))
    textFile.close()
    model = pwd + '/articles.ftz'
    label = os.popen("fasttext predict-prob "+model+" "+filePath).read()
    labels = str(label).replace('\n', '').split(" ")
    if len(labels) > 1 and labels[0] in labelDict.keys() and float(labels[1]) > 0.5:
        return labelDict[labels[0]]
    else:
        return labelDict["other"];

