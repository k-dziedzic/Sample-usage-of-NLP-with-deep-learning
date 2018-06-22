from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from heapq import nlargest
from collections import defaultdict

articleURL = "http://antyweb.pl/mysz-cooler-master-mastermouse-520/"


def getTextWaPo(url):
    req = Request(articleURL,headers={'User-Agent': 'Opera/53.0.2907.99'})
    page = urlopen(req).read().decode('utf8')
    soup = BeautifulSoup(page, "lxml")
    text = ' '.join(map(lambda p: p.text, soup.find_all("article")))
    return text.encode('utf8', errors='replace').decode().replace("?"," ")


text = getTextWaPo(articleURL)


def summarize(text, n):
    sents = sent_tokenize(text)
    word_sent = word_tokenize(text.lower())
    _stopword = set(stopwords.words('polish.txt') + list(punctuation))
    word_sent = [word for word in word_sent if word not in _stopword]
    freq = FreqDist(word_sent)
    ranking = defaultdict(int)

    for i, sent in enumerate(sents):
        for w in word_tokenize(sent.lower()):
            if w in freq:
                ranking[i] += freq[w]

    sents_idx = nlargest(n, ranking, key=ranking.get)
    return [sents[j] for j in sorted(sents_idx)]


print(summarize(text, 3))

