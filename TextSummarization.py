from urllib.request import urlopen
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from heapq import nlargest
from collections import defaultdict

articleURL = "https://www.washingtonpost.com/world/the_americas/the-chaotic-effort-to-reunite-immigrant-parents-with-their-separated-kids/2018/06/21/325cceb2-7563-11e8-bda1-18e53a448a14_story.html?utm_term=.e3a3943befb4"


def getTextWaPo(url):
    page = urlopen(articleURL).read().decode('utf8')
    soup = BeautifulSoup(page, "lxml")
    text = ' '.join(map(lambda p: p.text, soup.find_all('article')))
    return text


text = getTextWaPo(articleURL)


def summarize(text, n):
    sents = sent_tokenize(text)
    assert n < len(sents)
    word_sent = word_tokenize(text.lower())
    _stopword = set(stopwords.words('english') + list(punctuation))

    word_sent = [word for word in word_sent if word not in _stopword]
    freq = FreqDist(word_sent)

    ranking = defaultdict(int)

    for i, sent in enumerate(sents):
        for w in word_tokenize(sent.lower()):
            if w in freq:
                ranking[i] += freq[w]

    sents_idx = nlargest(4, ranking, key=ranking.get)
    return [sents[j] for j in sorted(sents_idx)]


print(summarize(text, 3))
