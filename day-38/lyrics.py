import requests
import os

endless = True

while endless:
    os.system('cls')
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
    print(f"\n{title_name.title()} by {artist_name.title()}")
    print("--------------------------------------------")
    print(song_lyrics['lyrics'])

    continue_program = input("\n\nContinue? (Y/N): ").lower()

    if continue_program == "n":
        endless = False

print("Program stopped.")
