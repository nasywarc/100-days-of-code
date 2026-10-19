from bs4 import BeautifulSoup

with open('website.html', 'r', encoding='utf-8') as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

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

heading = soup.find(name="h1", id="name")
print(heading)

heading_3 = soup.find(name="h3", class_="heading")
print(heading_3.getText())

name = soup.select_one("#name")
print(name)

headings = soup.select(".heading")
print(headings)
