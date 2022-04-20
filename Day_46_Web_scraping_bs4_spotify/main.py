import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
# from spotipy.oauth2 import SpotifyClientCredentials
from spotify_cert import client_secret,client_id

# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
#                                                            client_secret=client_secret))
# results = sp.search(q='dup lipa', limit=20)
# print(results)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                client_secret=client_secret,
                                                redirect_uri="http://example.com",
                                                scope= "playlist-modify-private",
                                                show_dialog=True,
                                                cache_path=r"D:\christine kao\VS Code\100 days\Day_43_We_scraping_song\token.txt"))

# Get detailed profile information about the current user.
user_id = sp.current_user()["id"]
# print(user_id)

date = input("What year do you want to travel to? Type the date in this format YYYY-MM-DD : ")
# song_names = ["The list of song", "titles from your", "web scrape"]

#-------------- list of songs which we create from scraping the billiboard website.--------------#
response = requests.get('https://www.billboard.com/charts/hot-100/'+date)

soup = BeautifulSoup(response.text,'html.parser')
# print(soup.prettify())

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.find_all("span", class_="chart-element__information__song")
song_names = [song.getText() for song in song_names_spans]
year = date.split("-")[0]

#---------------------- Search Spotify for the 100 Songs's URI with specific year  --------------------#
song_uris = []
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        # print(f"{song} doesn't exist in Spotify. Skipped.")
        pass

# print(song_uris)

#---------------------------- Get User's Playlist --------------------------------#
# playlist=[]
# user_playlists = sp.user_playlists(user_id)['items']
# for i in range(len(user_playlists)):
#     playlist.append(user_playlists[i]['name'])

#---------------------------- Creating and Adding to Spotify Playlist --------------------------------#
# create playlists
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

# Adds tracks/episodes to a playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

