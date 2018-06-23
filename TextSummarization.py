from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from heapq import nlargest
from collections import defaultdict
from langdetect import detect

articleURL = "http://antyweb.pl/elektronika-ograniczone-zaufanie/"


def getTextWaPo(url):
    req = Request(articleURL, headers={'User-Agent': 'Opera/53.0.2907.99'})
    page = urlopen(req).read().decode('utf8')
    soup = BeautifulSoup(page, "lxml")
    text = ' '.join(map(lambda p: p.text, soup.find_all('article')))
    if text:
        return text.encode('utf-8', errors='replace').decode().replace("\n", "")
    else:
        page = urlopen(articleURL).read().decode('utf8')
        soup = BeautifulSoup(page, "lxml")
        text = ' '.join(map(lambda p: p.text, soup.find_all('article')))
        return text.encode('utf-8', errors='replace').decode().strip()


text = getTextWaPo(articleURL)


def summarize(text, n):
    if text:
        sents = sent_tokenize(text)
        sents = sents[1:-1]

        assert n < len(sents), "The number of sentences that you want in the summary is too high from a possible"

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

        sents_idx = nlargest(n, ranking, key=ranking.get)
        return [sents[j] for j in sorted(sents_idx)]
    else:
        return "Empty \"div id=\"article\""


print(summarize(text, 4))
