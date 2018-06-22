# urllib to download website
from urllib.request import urlopen

# pip install beautifulsoup4
# BeautifulSoup to parse the website
from bs4 import BeautifulSoup

articleURL="https://www.washingtonpost.com/world/the_americas/the-chaotic-effort-to-reunite-immigrant-parents-with-their-separated-kids/2018/06/21/325cceb2-7563-11e8-bda1-18e53a448a14_story.html?utm_term=.e3a3943befb4"

page=urlopen(articleURL).read().decode('utf8', 'ignore')
soup= BeautifulSoup(page, "lxml")

# page in 'lxml' format
# print(soup)

# print(soup.find('article').text)

text=' '.join(map(lambda p: p.text, soup.find_all('article')))

print(text)


