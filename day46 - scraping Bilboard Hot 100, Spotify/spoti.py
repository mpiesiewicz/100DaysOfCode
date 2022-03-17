import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.exceptions import SpotifyException
from credentials import USER_ID, SECRET, URI
import time


class SpotiManager:
    def __init__(self, uri, secret, user_id):
        self.uri = uri
        self.secret = secret
        self.id = user_id
        self.scope = "playlist-modify-public"
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(self.id, self.secret, self.uri, scope=self.scope))

    def create_playlist(self):
        songs, date = self.scrape_billboard()
        songs_spotify_ids = self.get_spotify_uris(songs)
        self.fill_playlist(date, songs_spotify_ids)
        print('Done!')

    @staticmethod
    def scrape_billboard():
        date = input('Which year would you like to travel to? (YYY-MM-DD format): ')
        # date = '1994-04-13'

        url = f'https://www.billboard.com/charts/hot-100/{date}'
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')

        artists = soup.select(selector='li ul li span.c-label.a-no-trucate')
        titles = soup.select(selector='li ul li h3.c-title.a-no-trucate')

        titles = [title.getText().strip() for title in titles]
        artists = [artist.getText().strip() for artist in artists]

        return [f'{artist[:10]} {titles[number][:10]}' for number, artist in enumerate(artists)], date

    def get_spotify_uris(self, songs):
        results_list = list()
        for song in songs:
            try:
                result = self.sp.search(song, limit=1, type='track', market='US')
                result_id = result['tracks']['items'][0]['uri']
            except IndexError:
                print(f'Error: song {song} not found.')
            except SpotifyException:
                print(f'Error: Spotify related for song {song}')
            else:
                results_list.append(result_id)
            finally:
                time.sleep(5)
        return results_list

    def fill_playlist(self, date, songs_spotify_ids):
        playlist_name = f'Billboard Hot 100 - {date}'
        my_user_uri = self.sp.me()['uri'].split(':')[2]
        new_playlist = self.sp.user_playlist_create(my_user_uri, playlist_name)
        new_playlist_id = new_playlist['id']
        self.sp.playlist_add_items(new_playlist_id, songs_spotify_ids)


# manager = SpotiManager(URI, SECRET, USER_ID)
# manager.create_playlist()
#
