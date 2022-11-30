

from flask import Flask, render_template
import os
import requests
import json
import random
from method import getToken, getArtistInfo, getTracks , getLyrics 
from test_data import gettestArtistInfo, gettestTracks
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv()) # This is to load your API keys from .env

# declaring app name
app = Flask(__name__)
 
