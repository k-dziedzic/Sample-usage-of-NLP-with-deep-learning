from urllib.request import urlopen
from bs4 import BeautifulSoup

articleURL="https://www.washingtonpost.com/world/the_americas/the-chaotic-effort-to-reunite-immigrant-parents-with-their-separated-kids/2018/06/21/325cceb2-7563-11e8-bda1-18e53a448a14_story.html?utm_term=.e3a3943befb4"

def getTextWaPo(url):
    page = urlopen(articleURL).read().decode('utf8')
    soup=BeautifulSoup(page,"lxml")
    text = ' '.join(map(lambda p: p.text, soup.find_all('article')))
    return text

text=getTextWaPo(articleURL)
print(text)

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation

import nltk
nltk.download('punkt')
sents = sent_tokenize(text)
# print(sents)

word_sent = word_tokenize(text.lower())
# print(word_sent)

nltk.download('stopwords')
_stopword = set(stopwords.words('english') + list(punctuation))
# print(_stopword)

word_sent = [word for word in word_sent if word not in _stopword]
print(word_sent)

from nltk.probability import FreqDist
freq = FreqDist(word_sent)
# print(freq)

from heapq import nlargest
nlargestWord = nlargest(10,freq, key=freq.get)
# print(nlargestWord)

from collections import defaultdict
ranking = defaultdict(int)

for i, sent in enumerate(sents):
     for w in word_tokenize(sent.lower()):
        if w in freq:
            ranking[i] += freq[w]

# print(ranking)

sents_idx = nlargest(4, ranking, key=ranking.get)
# print(sents_idx)

print([sents[j] for j in sorted(sents_idx)])
