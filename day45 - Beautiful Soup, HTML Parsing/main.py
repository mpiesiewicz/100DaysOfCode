from bs4 import BeautifulSoup
import requests

response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')

# article_text = titles.getText()
# article_link = titles.get('href')
# article_upvote = soup.find(name='span', class_='score').getText()
#
# print(article_text, article_link, article_upvote)


titles = soup.findAll(name='h3', class_='title')

list = [title.getText() for title in titles[::-1]]
print(list)
