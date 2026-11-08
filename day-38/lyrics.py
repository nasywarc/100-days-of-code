import requests

artist_name = input("Type artist name: ")
title_name = input("Type title name: ")

end_point = (f"https://api.lyrics.ovh/v1/{artist_name}/{title_name}")

headers = {
    "Content-Type": "application/json"
}

response = requests.get(
    url=end_point,
    headers=headers,
)

song_lyrics = response.json()
print(song_lyrics['lyrics'])
