from urllib import response
import requests
import json



search_token="BQCowN_TBBVyFPmrHwI6xmCf5CnZRyaY2OmZW8_y8qDT3vJaJb3q48RhgXtf38UoFyP40qQCAtXD0ueDMQvTxdHe50nJg6aeQW6heUoN3MgwPPOvrOs18FhGxkitPIXZyEjE1UrfOp7ccBWcBfSZkXDMJ_5mLbEQkF6nRsEn5A6SJqopHUjr1QiXs_Rnlrdy50o"
add_token="BQCTF5NWeMGn0GkWxYsrV4LIXYoA3s4Rr_V5cjQS9V7fNVpCWDr0Y2xlrB_Jki-OxH5fXJwFRyy_r64gDeQX2BjvzO1eV6k3TYmEAlaDsscilv3Z48eXyS4D71-csYPp0y6-fupVdci9FnoNh5HXu7ozI94w_jm9CQdzgzlCBNwOJw2iTZOfx99CVD2DBS2_jOVUMQTJVhJTpSLBDlPbJqoltP7RPvFvAyxbq9kdekT2Qm2KhSpU9Q9v9BJ3kJHK"
spotify_url = 
secret_token=

class SpotifyClient(object):
    def __init__(self,api_token):
        self.api_token=api_token
    
    def add_song_to_spotify(self,all_song_info):
        playlist_id="2HrhEwtyoltxmriwMoDTYt?si=367f14ba606740bc"
        
        uris=[]
        for song, info in all_song_info.items():
            uris.append(info["spotify_uri"])
        
        request_body=json.dumps({"uris":uris})
        request_data = json.dumps(uris)
        query="https://api.spotify.com/v1/playlists/2HrhEwtyoltxmriwMoDTYt/tracks"  
        response=requests.post(
            query,
            data=request_data,
            headers ={
                "Content-Type": "application/json",
                "Authorization": "Bearer{}".format(add_token),
            },
            json={
            "uris": ["uris"],"position": 0},
        )
        print(uris)
        respone_json=response.json()
        print(response.status_code)
        return response.json
    
