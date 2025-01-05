import spotipy
from spotipy.oauth2 import SpotifyOAuth
from kafka import KafkaProducer
import json
import time
from dotenv import load_dotenv
import os

load_dotenv()


SPOTIPY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIFY_SECRET_KEY")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope="user-read-playback-state,user-read-currently-playing"
))

# current_track = sp.current_playback()
# if current_track and current_track['is_playing']:
#     track_name = current_track['item']['name']
#     artist_name = current_track['item']['artists'][0]['name']
#     print(f"Now Playing: {track_name} by {artist_name}")
# else:
#     print("No track currently playing.")

# Kafka setup
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Stream data from Spotify and send to Kafka
while True:
    current_track = sp.current_playback()
    if current_track and current_track['is_playing']:
        track_info = {
            'track_name': current_track['item']['name'],
            'artist_name': current_track['item']['artists'][0]['name'],
            'album_name': current_track['item']['album']['name'],
            'played_at': current_track['timestamp']
        }
        producer.send('spotify-data', value=track_info)
        print(f"Sent to Kafka: {track_info}")
    else:
        print("No track currently playing.")
    
    time.sleep(5)  # Fetch data every 5 seconds



