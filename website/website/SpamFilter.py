import os
import pyensae

pathToDatasets = "E:\PyCharmWorkspace\SampleUsageOfNLPWithDeepLearning\website\dataSources\enron"

#download data OnlineNewsPopularity
pyensae.download_data("enron1.tar.gz", url="http://www.aueb.gr/users/ion/data/enron-spam/preprocessed/", whereTo="E:\PyCharmWorkspace\SampleUsageOfNLPWithDeepLearning\website\dataSources\enron")
pyensae.download_data("enron2.tar.gz", url="http://www.aueb.gr/users/ion/data/enron-spam/preprocessed/", whereTo="E:\PyCharmWorkspace\SampleUsageOfNLPWithDeepLearning\website\dataSources\enron")
pyensae.download_data("enron3.tar.gz", url="http://www.aueb.gr/users/ion/data/enron-spam/preprocessed/", whereTo="E:\PyCharmWorkspace\SampleUsageOfNLPWithDeepLearning\website\dataSources\enron")
pyensae.download_data("enron4.tar.gz", url="http://www.aueb.gr/users/ion/data/enron-spam/preprocessed/", whereTo="E:\PyCharmWorkspace\SampleUsageOfNLPWithDeepLearning\website\dataSources\enron")
pyensae.download_data("enron5.tar.gz", url="http://www.aueb.gr/users/ion/data/enron-spam/preprocessed/", whereTo="E:\PyCharmWorkspace\SampleUsageOfNLPWithDeepLearning\website\dataSources\enron")
pyensae.download_data("enron6.tar.gz", url="http://www.aueb.gr/users/ion/data/enron-spam/preprocessed/", whereTo="E:\PyCharmWorkspace\SampleUsageOfNLPWithDeepLearning\website\dataSources\enron")

# print folders, subfolders and number of files in subfolder
# for folders, subfolders, files in os.walk(pathToDatasets):
#     print(folders, subfolders, len(files))
#
# check how to build path
# print(os.path.split(pathToDatasets))
# print(os.path.split(pathToDatasets)[0])
# print(os.path.split(pathToDatasets)[1])

# Print the ham and spam folders
# for folders, subfolders, files in os.walk(pathToDatasets):
#     if (os.path.split(folders)[1] == 'ham'):
#         print(folders, subfolders, len(files))
#
#     if (os.path.split(folders)[1] == 'spam'):
#         print(folders, subfolders, len(files))

ham_list = []
spam_list = []

# Read the files and join ham and spam list

for directories, subdirs, files in os.walk(pathToDatasets):
    if (os.path.split(directories)[1] == 'ham'):
        for filename in files:
            with open(os.path.join(directories, filename), encoding="latin-1") as f:
                data = f.read()
                ham_list.append(data)

    if (os.path.split(directories)[1] == 'spam'):
        for filename in files:
            try:
                with open(os.path.join(directories, filename), encoding="latin-1") as f:
                    data = f.read()
                    spam_list.append(data)
            except:
                print(filename)

print(ham_list[0])
print(spam_list[0])
