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

#genius api for song lyrics   

def getLyrics(track, artist):
    headers = {
        'Authorization': 'Bearer {token}'.format(token=os.getenv('genius_token')),
    }
    
    #split the track string when hit "(" and "-" and return first element
    #Concatenation and replace white space with '%20'
    search = (track.split("(")[0].split("-")[0] + artist).replace(" ", "%20")   
    
    songInfo = requests.get("http://api.genius.com/search?q=" + search, headers=headers).json()
   
    try: 
        song_path = songInfo["response"]["hits"][0]["result"]["api_path"]
        track = requests.get("http://api.genius.com" + song_path, headers=headers).json()
        
        path= track['response']["song"]["path"]
        # print()
        # print(path)
        
        return path
    
    except: 
        return "/Lyrics%20not%20found!!!"