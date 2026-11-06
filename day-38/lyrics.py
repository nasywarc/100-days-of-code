import requests

end_point = "https://api.lyrics.ovh/v1/"
data_params = {
    'artist': "",
    'title': "",
}

artist_name = input("Type artist name: ")
title_name = input("Type title name: ")
