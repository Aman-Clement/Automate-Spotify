import os


from requests import request
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import requests
import urllib

search_token="BQCowN_TBBVyFPmrHwI6xmCf5CnZRyaY2OmZW8_y8qDT3vJaJb3q48RhgXtf38UoFyP40qQCAtXD0ueDMQvTxdHe50nJg6aeQW6heUoN3MgwPPOvrOs18FhGxkitPIXZyEjE1UrfOp7ccBWcBfSZkXDMJ_5mLbEQkF6nRsEn5A6SJqopHUjr1QiXs_Rnlrdy50o"

songs=[]
all_song_info = {}

def get_spotify_uri(song_name,artist):
        query=urllib.parse.quote(f'{artist} {song_name}')
        url ="https://api.spotify.com/v1/search?q={}&type=track".format(query)
        response = requests.get(url,headers={
        "Content-Type":"application/json","Authorization": "Bearer {}".format(search_token)
    })
        response_json = response.json()
        songs = response_json["tracks"]["items"]
        #only use the first song
        try:
            uri = songs[0]["uri"]
        except IndexError:
            uri = 'null'
        return uri
# class Playlist(object):
#     def __init__(self,id,title):
#         self.id=id
#         self.title=title
        
class Song(object):
    def __init__(self,artist,track):
        self.artist=artist
        self.track=track

class YoutubeClient(object):
    def __init__(self,project_id):
        # CLIENT_SECRETS_FILE = 'client_secret.json'
        # This OAuth 2.0 access scope allows for full read/write access to the
        # authenticated user's account.
        SCOPES = ['https://www.googleapis.com/auth/youtube']
        API_SERVICE_NAME = 'youtube'
        API_VERSION = 'v3'
        
        os.environ["OUATHLIB_INSECURE_TRANSPORT"]="1"
        client_secrets_file="YOUR_CLIENT_SECRET.json"
        # ACTIONS = ('get', 'list', 'set')

        # Authorize the request and store authorization credentials.
        flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file, SCOPES)
        # flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(credentials_location, SCOPES)
        credentials = flow.run_console()
        youtube_client=build(API_SERVICE_NAME, API_VERSION, credentials = credentials)
        self.youtube_client = youtube_client

   
    def get_playlists(self):
        playlist_id='PLxWiyJISqBm_mgJ0JvNVXgO-1zemacgvf'#paste id herer
        pl_request = self.youtube_client.playlistItems().list(
            part='content Details',playlistId=playlist_id,maxResults=50,
        )
        pl_response = pl_request.execute()
        # nextPageToken =pl_response.get('nextPageToken')
        return pl_response
        
        # to iterate over every video in the playlist and get the ID.
    
    def get_vedios_from_playlist(self, pl_response):
        vid_ids = []
        for item in pl_response['items']:
            vid_ids.append(item['contentDetails']['videoId'])
        vid_request = self.youtube_client.videos().list(
            part="snippet",id=",".join(vid_ids)
        )
        vid_response = vid_request.execute()
        # save video title, youtube URL
        
        for item in vid_response["items"]:
            video_title = item["snippet"]["title"]
            print (video_title)
            youtube_url = "https://www.youtube.com/watch?v={}".format(item["id"])
            print(youtube_url)
            x,y=video_title.split('-')
            print(y)
            print(x)
            spotify_uri = get_spotify_uri(y,x)
            print(spotify_uri)
            if(spotify_uri!='null'):
                all_song_info[video_title] = {"youtube_url": youtube_url, "song_name": y, "spotify_uri": spotify_uri}
        print(len(all_song_info))
        print(all_song_info)
        return all_song_info
    #         artist.append(x)
    #         song_name.append(y)
            # print (video_title)
            # youtube_url = "https://www.youtube.com/watch?v={}".format(item["id"])
            # #use youtube_dl to collect the song_name and artist name
            # video = youtube_dl.YoutubeDL({}).extract_info(youtube_url,download=False)
            # try:
            #     #extract the track name, artist and the spotify uri and save them in our dict
            #     song_name = video["track"]
            #     print(song_name)
            #     artist = video["artist"]
            #     print(artist)
            # except KeyError as e:
            #     print("Current song details are unavailable ")
    
        # print(len(all_song_info))
        # print(all_song_info)
        # return all_song_info
    
    
    
    
    
    
    
    
    
    
    
    # def get_playlists(self):
    #     request=self.youtube_client.playlists().list(
    #         # part="content Details",
    #         part="id, snippet",
    #         # playlistId="playlist_id",
    #         maxResults=50,
    #         mine=True,
    #         # pageToken=nextPageToken
    #     )

    #     response =request.execute()
        
    #     playlists = [Playlist(item['id'],item['snippet']['title']) for item in response['items']]
    #     return playlists

    # def get_vedios_from_playlist(self, playlist_id):
    # #     vedio_id=[]
    # #     for item in playlists:
    # #         vedio_id.appen
        
        
    #     songs=[]
    #     request = self.youtube_client.playlistItems().list(
    #         playlistId=playlist_id,
            
    #         part="id,snippet"
    #     )

    #     response=request.execute()

    #     for item in response['items']:
    #         vedio_id=item['snippet']['resourceId']['videoId']
    #         artist,track = self.get_artist_and_music_from_vedio(vedio_id)
    #         if artist and track:
    #             songs.append(Song(artist,track))
        
    #     return songs
                



    # def get_artist_and_music_from_vedio(self,vedio_id):
    #     youtube_url=f"https://www.youtube.com/watch?v={vedio_id}"

    #     video = youtube_dl.YoutubeDL({'quiet':True}).extract_info(
    #         youtube_url,
    #         download=False
    #     )
    #     try:
    #         track=video["track"]
    #         print(track)
    #         artist=video["artist"]
    #         print(artist)
    #         return artist,track
    #     except:
    #         print("details not available")
    #         return None
    
        