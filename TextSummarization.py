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