import os

labelDict = {"__label__political": "Polityczny",
             "__label__sport": "Sportowy",
             "__label__technology": "Techniczny",
             "other": "Inny"}


def classify(text):
    """
    Dla Windows, konieczne jest dodanie lokalizacji folderu exe do zmiennych środowiskowych,
    tak żeby fasttext można było uruchomić z poziomu wiersza poleceń
    """
    pwd = os.path.dirname(__file__)
    file_path = pwd + '/text.txt'
    text_file = open(file_path, "w", encoding="utf8")
    text_file.write(text.replace('\n', ' '))
    text_file.close()
    model = pwd + '/articles.ftz'
    label = os.popen("fasttext predict-prob "+model+" "+file_path).read()
    labels = str(label).replace('\n', '').split(" ")
    if len(labels) > 1 and labels[0] in labelDict.keys() and float(labels[1]) > 0.5:
        return labelDict[labels[0]]
    else:
        return labelDict["other"]


# from pyfasttext import FastText
#
#
# def classify(text):
#     """Dla Linux i MAC OS, ponieważ pyfasttext korzysta z cysignals które nie jest dostępne na platformy Windows"""
#     pwd = os.path.dirname(__file__)
#     model_path = pwd + '/articles.ftz'
#     text2 = text.replace('\n', ' ')+"\n";
#     model = FastText(model_path)
#     label = model.predict_proba_single(text2, k=1)
#     str = "__label__"+ label[0][0]
#     if len(label) > 0 and str in labelDict.keys() and float(label[0][1]) > 0.5:
#         return labelDict[str]
#     else:
#         return labelDict["other"]
