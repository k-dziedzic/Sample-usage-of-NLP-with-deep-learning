import glob
import json

# path = 'D:\\Studia\\Semestr VI\\Sztuczna inteligencja\\technology\\*.json'
# files = glob.glob(path)
# label = ""
# print(len(files))
# for file in files:
#     jsonFile = open(file, 'rU', encoding="utf8", errors='ignore')
#     values = json.load(jsonFile)
#     text = values['text']
#     label += "__label__technology "+text.replace('\n', ' ')+"\n"
#     jsonFile.close()
#
#
# print(len(files))
# text_file = open("../../technology_train.txt", "w", encoding="utf8")
# text_file.write(label)
# text_file.close()
#
#
# path = 'D:\\Studia\\Semestr VI\\Sztuczna inteligencja\\political\\*.json'
# files = glob.glob(path)
# label = ""
# print(len(files))
# for file in files:
#     jsonFile = open(file, 'rU', encoding="utf8", errors='ignore')
#     values = json.load(jsonFile)
#     text = values['text']
#     label += "__label__political "+text.replace('\n', ' ')+"\n"
#     jsonFile.close()
#
#
# print(len(files))
# text_file = open("../../political_train.txt", "w", encoding="utf8")
# text_file.write(label)
# text_file.close()


path = 'D:\\Studia\\Semestr VI\\Sztuczna inteligencja\\sport\\*.json'
files = glob.glob(path)
label = ""
print(len(files))
for file in files:
    jsonFile = open(file, 'rU', encoding="utf8", errors='ignore')
    values = json.load(jsonFile)
    text = values['text']
    label += "__label__sport "+text.replace('\n', ' ')+"\n"
    jsonFile.close()


print(len(files))
text_file = open("../../sport_train.txt", "w", encoding="utf8")
text_file.write(label)
text_file.close()
