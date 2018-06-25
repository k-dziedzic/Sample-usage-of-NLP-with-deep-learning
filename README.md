# Sample usage of NLP with deep learning

## Overview
A application built with Django Framework. Allows you to summarize text from web pages or provided by the user. Enables the option of assigning categories to a given text (sports, political etc.). It also provides an anti-spam filter. The last two functionalities use models trained on datasets from<br/><br/>
https://webhose.io/datasets/<br/>
http://www2.aueb.gr/users/ion/data/enron-spam/<br/>

## How to run?
1. Go to catalog "website".
2. Run terminal.
3. Enter "python manage.py runserver".
4. Go to http://127.0.0.1:8000

## Environment
PyCharm Community Edition 2017.2.4<br/>
Build #PC-172.4343.24, built on October 19, 2017<br/>
JRE: 1.8.0_152-release-915-b12 amd64<br/>
JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o<br/>
Windows 10 10.0<br/>

If you want all functionalities to work properly, you must move all file in catalog "exe" to catalog where you have Python (ex. C:\Users\<UserName>\AppData\Local\Programs\Python\Python36-32\Scripts)

## Used libraries
- nltk
- pyensae 
- os
- pickle
- urllib
- bs4
- heapq
- langdetect
- string
- collections
- random
- glob
- json
- fastText
