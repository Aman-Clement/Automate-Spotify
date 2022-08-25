from spotify_client import SpotifyClient
from youtube_client import YoutubeClient
from spotify_client import SpotifyClient
import os
import socket
socket.getaddrinfo('localhost', 80)

def run():
    youtube_client=YoutubeClient('./creds/client_secret.json')
    spotify_client=SpotifyClient(os.getenv('SPOTIFY_AUTH_TOKEN'))
    playlists = youtube_client.get_playlists()
    
    # for index,playlist in enumerate(playlists):
    #     print(f"{index}:{playlist.title}")
    # choice=int(input("Enter your choice: "))
    # chosen_playlist=playlists[choice]
    #doesnt work anymore plz hardcode
    # print(f"You have selected:{chosen_playlist.title}")
    playlist_id="2HrhEwtyoltxmriwMoDTYt?si=8157f6f8de814aaa"
    all_song_info=youtube_client.get_vedios_from_playlist(playlists)
    # for song in all_song_info:
    #     spotify_song_id=spotify_client.search_song(song.artist,song.track)
    #     if spotify_song_id:
    #         added_song=spotify_client.add_song_to_spotify(spotify_song_id,playlist_id)
    #         if added_song:
    #             print(f"Added {song.artist}")
    
    spotify_client.add_song_to_spotify(all_song_info)
    
if __name__=='__main__':
    run()