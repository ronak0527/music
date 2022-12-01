##TOOLS/FRAMEWORKS USED:

Flask 

Spotify API

Genuis API

Basic HTML/CSS for front-end

python for back-end


SETTING UP PROJECT
--------------------------------------------------------------------------------------------------------------

1.Clone the repository

    https://github.com/ronak0527/music.git

2.Set Up Environment Variables Create a .env file with access keys to be used to access the Spotify API and Genius API. It is a hidden file. Contents of secrets.env:

    #Spotify
    export SPOTIFY_CLIENT_ID=(Spotify Client ID)
    export SPOTIFY_CLIENT_SECRET=(Spotify Client Secret)

    #Genius
    export genius_token=(Genius_TOKEN)

3.Create a gitgnore file to hide the secret acces file names:
 
    .env

4.Install required Python Packages

    pip install flask
    pip install requests
    pip install python-dotenv
    pip install random