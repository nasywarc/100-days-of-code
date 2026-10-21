import requests
from bs4 import BeautifulSoup

response_billboard = requests.get("https://www.billboard.com/charts/hot-100/")
billboard_webpage = response_billboard.text

bb_soup = BeautifulSoup(billboard_webpage, "html.parser")

title_tag = bb_soup.select(
    '.c-title.a-font-basic.u-letter-spacing-0010.u-max-width-397.lrv-u-font-size-16')
top_100 = []
for tag in title_tag:
    top_100.append(tag.getText(strip=True))

singer_tag = bb_soup.select(
    'span.c-label.a-no-trucate.a-font-secondary')
singer_list = []
for tag in singer_tag:
    singer_list.append(tag.getText(strip=True))

with open('top_100_211026.txt', 'w') as file:
    for num_song in range(len(top_100)):
        info = f'Top #{num_song+1} song is {top_100[num_song]} by {singer_list[num_song]}'
        print(info)
        file.write(info + '\n')
