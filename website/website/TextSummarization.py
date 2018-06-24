from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from heapq import nlargest
from collections import defaultdict
from langdetect import detect
from random import randint

def getTitle(url):
    req = Request(url, headers={'User-Agent': 'Chrome'})
    soup = BeautifulSoup(urlopen(req).read().decode('utf8'), "lxml")
    title= soup.title.text

    req1 = Request(url)
    try:
        soup1 = BeautifulSoup(urlopen(req1).read().decode('utf8'), "lxml")
        title1 = soup1.title.text
    except:
        if title is not "None":
            return title
        else:
            return "Strona wykorzystuje znaczniki nie dostosowane do wyszukiwania tytułu"

    if title1>=title:
        if title1 is not "None":
            return title1
        else:
            return "Strona wykorzystuje znaczniki nie dostosowane do wyszukiwania tytułu."

def textWithoutJS(soup):
    for script in soup(["script", "style"]):
        script.decompose()


def getTextFromWebsite(url):
    request = Request(url, headers={'User-Agent': 'Opera/53.0.2907.99'})
    website = urlopen(request).read().decode('utf8','ignore')
    beautifulSoup = BeautifulSoup(website, "lxml")
    textWithoutJS(beautifulSoup)

    text = ' '.join(map(lambda p: p.text, beautifulSoup.find_all('article')))

    if text:
        return text.encode('utf8', errors='replace').decode().translate(str.maketrans("\n\r\t","   ")).replace(".",". ")
    else:
        website = urlopen(url).read().decode('utf8','ignore')
        beautifulSoup = BeautifulSoup(website, "lxml")
        textWithoutJS(beautifulSoup)
        text = ' '.join(map(lambda p: p.text, beautifulSoup.find_all('article')))
        return text.encode('utf8', errors='replace').decode().strip().translate(str.maketrans("\n\r\t","   ")).replace(".",". ")


def deleteRepeatingSentence(sents):
    for i in range (0, len(sents)):
        for j in range (i+1, len(sents)-1):
            if sents[i]==sents[j]:
                for k in range (j,len(sents)-1):
                    sents[j]=sents[j+1]

def summarize(text, n):
    if text:
        sents = sent_tokenize(text)
        deleteRepeatingSentence(sents)
        if int(n)<len(sents):
            word_sent = word_tokenize(text.lower())

            if detect(sents[randint(0, len(sents))]) == "en":
                _stopword = set(stopwords.words('english') + list(punctuation))
            else:
                _stopword = set(stopwords.words('polish.txt') + list(punctuation))

            word_sent = [word for word in word_sent if word not in _stopword]

            frequency = FreqDist(word_sent)
            ranking = defaultdict(int)

            for i, sent in enumerate(sents):
                for w in word_tokenize(sent.lower()):
                    if w in frequency:
                        ranking[i] += frequency[w]

            sents_id = nlargest(int(n), ranking, key=ranking.get)

            return [sents[j] for j in sorted(sents_id)]

        else:
            return "Określona liczba zdań streszczenia przekracza liczbę wszystkich zdań artykułu."

    else:
        return "Strona wykorzystuje znaczniki nie dostosowane do wyszukiwania artykułu."

