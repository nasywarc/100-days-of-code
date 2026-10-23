import requests
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic

load_dotenv()

date = '2025-09-27'
header = {
    'user-agent': os.getenv('user-agent')
}
response = requests.get(
    url=f'https://appbrewery.github.io/bakeboard-hot-100/{date}/',
    headers=header,
)

bb_soup = BeautifulSoup(response.text, "html.parser")

song_tag = bb_soup.select('.chart-entry__title')
song_list = []
for song in song_tag:
    song_list.append(song.getText())

yt = YTMusic('browser.json')
playlists = yt.get_library_playlists()

duplicate = False
for playlist in playlists:
    if playlist['title'] == f'BB 100 {date}':
        duplicate = True

if duplicate == False:
    new_playlist = yt.create_playlist(
        title=f'BB 100 {date}',
        privacy_status='PRIVATE',
        description=f'New Playlist for BB 100 {date}',
        )
    for song in range (len(song_list)):
        search_results = yt.search(song_list[song])
        yt.add_playlist_items(
            playlistId=new_playlist,
            videoIds=[search_results[0]['videoId']],
        )
        print(f'The song of {song_list[song]} has been added to the playlist as the {song+1}th')
    
else:
    print('Already have that playlist name.')
