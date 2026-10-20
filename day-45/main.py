from bs4 import BeautifulSoup
import requests

# with open('website.html', 'r', encoding='utf-8') as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")

# print(soup)
# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# all_anchor_tags = soup.find_all(name="a")
# for tag in all_anchor_tags:
#     print(tag.getText())
# for tag in all_anchor_tags:
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# heading_3 = soup.find(name="h3", class_="heading")
# print(heading_3.getText())

# name = soup.select_one("#name")
# print(name)

# headings = soup.select(".heading")
# print(headings)

# scraping a live website

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

article_tag = soup.find(class_='titleline')
article_text = article_tag.find('a').getText()
article_link = article_tag.find('a').get('href')
article_upvote = soup.find(name='span', class_="score").string
print(article_text)
print(article_link)
print(article_upvote)
