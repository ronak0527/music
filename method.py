import requests
import json
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv()) # This is to load your API keys from .env

def getToken():
    data = {
        'grant_type':'client_credentials',
        'client_id':os.getenv('spotify_clientID'),
        'client_secret':os.getenv('spotify_secret'), 
    };

    token=requests.post("https://accounts.spotify.com/api/token", data = data).json()
    return token["access_token"]
    
def getArtistInfo(rand_id):
    headers = {
        'Authorization': 'Bearer {token}'.format(token=getToken())
    }
    artistInfo = requests.get("https://api.spotify.com/v1/artists/" + rand_id, headers=headers)
    return artistInfo.json()
    
def getTracks(rand_id):
    headers = {
        'Authorization': 'Bearer {token}'.format(token=getToken()),
    }
    tracks = requests.get("https://api.spotify.com/v1/artists/" + rand_id + "/top-tracks?market=US", headers=headers).json()["tracks"]
    
    trackList = []
    for track in tracks[0:10]:
        trackList.append(track)
        
    return trackList