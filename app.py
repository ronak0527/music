from flask import Flask, render_template
import os
import random
from method import getToken, getArtistInfo, getTracks , getLyrics 
from test_data import gettestArtistInfo, gettestTracks
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv()) # This is to load your API keys from .env

# declaring app name
app=Flask(__name__,template_folder='template')
 
# defining home page   
@app.route('/')
def index():

    #Artist ID from spotify 
    artists=["4YRxDV8wJFPHPTeXepOstw", "3xU8YsNNkmWSPewlB18NUz", "5f4QpKfy7ptCHwTqspnSJI","6vWDO969PvNqNYHIOW5v0m"]
    rand_id = random.choice(artists)
    
    try: 
        artistInfo = getArtistInfo(rand_id)
        tracks = getTracks(rand_id)
        
    except:
        artistInfo = gettestArtistInfo()
        tracks = gettestTracks()
   
    trackList = []
    for track in tracks:
        trackList.append(track)
        
    lyrics = []
    for track in trackList:
        lyrics.append("http://genius.com" + getLyrics(track["name"], artistInfo["name"]))
    
    #returning index.html
    return render_template(
        "index.html",
        artistImg =artistInfo["images"][0]["url"],
        artistName =artistInfo["name"],
        tracks=getTracks(rand_id),
        tracksLen = len(tracks),
        lyrics=lyrics,
        )

# running app 
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)