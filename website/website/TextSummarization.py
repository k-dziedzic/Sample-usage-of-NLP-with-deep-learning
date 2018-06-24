from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from heapq import nlargest
from collections import defaultdict
from langdetect import detect

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
            return "Strona wykorzystuje znaczniki nie dostosowane do wyszukiwania"

    if title1>=title:
        if title1 is not "None":
            return title1
        else:
            return "Strona wykorzystuje znaczniki nie dostosowane do wyszukiwania"

def textWithoutJS(soup):
    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.decompose()  # rip it out

def getTextWaPo(url):
    req = Request(url, headers={'User-Agent': 'Opera/53.0.2907.99'})
    page = urlopen(req).read().decode('utf8')
    soup = BeautifulSoup(page, "lxml")
    textWithoutJS(soup)
    text = ' '.join(map(lambda p: p.text, soup.find_all('article')))
    if text:
        return text.encode('utf-8', errors='replace').decode().replace("?", " ").replace(".",". ")
    else:
        page = urlopen(url).read().decode('utf8')
        soup = BeautifulSoup(page, "lxml")
        textWithoutJS(soup)
        text = ' '.join(map(lambda p: p.text, soup.find_all('article')))
        return text.encode('utf-8', errors='replace').decode().strip().replace("?", " ").replace(".",". ")

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

            if detect(sents[3]) == "en":
                _stopword = set(stopwords.words('english') + list(punctuation))
            else:
                _stopword = set(stopwords.words('polish.txt') + list(punctuation))

            word_sent = [word for word in word_sent if word not in _stopword]

            freq = FreqDist(word_sent)
            ranking = defaultdict(int)

            for i, sent in enumerate(sents):
                for w in word_tokenize(sent.lower()):
                    if w in freq:
                        ranking[i] += freq[w]

            sents_idx = nlargest(int(n), ranking, key=ranking.get)
            return [sents[j] for j in sorted(sents_idx)]

        else:
            return "The number of sentences that you want in the summary is too high from a possible"

    else:
        return "No \"div id=\"article\""

