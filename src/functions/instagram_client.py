import os
from dotenv import load_dotenv
from instagrapi import Client

class InstagramClient:
    def __init__(self):
        load_dotenv()
        self._client = Client()
        self._user_id = None
    
    def login(self):
        """Login to Instagram"""
        username = os.getenv('INSTAGRAM_USERNAME')
        password = os.getenv('INSTAGRAM_PASSWORD')
        self._client.login(username, password)
        self._user_id = self._client.user_id
        return self

    @property
    def client(self):
        return self._client

    @property
    def user_id(self):
        return self._user_id
