from django.apps import AppConfig
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class AppConfig(AppConfig):
    name = 'app'
