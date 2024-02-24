import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random
auth_manager = SpotifyOAuth(client_id="client-id",
                            client_secret="client-secret",
                            redirect_uri="http://google.com/",
                            scope="user-library-read user-top-read playlist-modify-public")
class SpotifyBot:
    def __init__(self):
        self.spotify = spotipy.Spotify(auth_manager=auth_manager)
        self.user_id = '31ojsle5q4bh3bewzlqqy32xazuu'
    def top_artists_id(self):
        top_artists = self.spotify.current_user_top_artists(limit=20)
        artists_ids = []
        for artists in top_artists["items"]:
            artists_ids.append(artists['id'])
        return artists_ids
    def top_songs(self):
        artist_list = self.top_artists_id()
        artist_name = "The Smiths"
        final_song_list = []
        for artists_id in artist_list:
            top_songs = self.spotify.artist_top_tracks(artists_id, "US")
            for songs in top_songs["tracks"]:
                random_select = random.getrandbits(1)
                if random_select == 0:
                    final_song_list.append(songs["id"])
        return final_song_list
    def create_playlist(self):
        track_id = self.top_songs()
        self.spotify.playlist_add_items("4uTOXx3fasMVh65pAlE7wS", track_id, position=None)

spotify_bot = SpotifyBot()
spotify_bot.create_playlist()

