import requests
import os
from dotenv import load_dotenv

load_dotenv()

"""https://the-odds-api.com is a free API that allows you to to query across several different Sports books. They 
have several different subscriptions but for their API but I used the free licence which allows around 500 request 
per month."""


class APIClient:
    """Handles communication with the Odds API."""

    def __init__(self):
        self.api_key = os.getenv("API_KEY")  # API_KEY
        self.base_url = "https://api.the-odds-api.com/v4"  # Base endpoint URL

    def get_sports(self):
        """Fetches a list of available sports."""
        endpoint = "/sports"  # Endpoint for getting sports
        params = {"api_key": self.api_key}  # Parameters for endpoint ( API-key)
        response = requests.get(f"{self.base_url}{endpoint}", params=params)  # Sending a get request and caching
        # repsonse
        response.raise_for_status()  # Raise an exception for error status codes (important we don't handle as they
        # rate limit API)
        sports_data = response.json()  # Get Response's json containing sports data

        return sports_data

    def get_odds(self, sport_key):
        """Fetches odds for a specific sport."""
        endpoint = "/sports/" + sport_key + "/odds/"  # Endpoint for getting odds and events
        params = {"api_key": self.api_key, "sport_key": sport_key, "regions": "us,us2"}  # Parameters for endpoint (
        # API-key, and sport)
        response = requests.get(f"{self.base_url}{endpoint}", params=params)  # Sending a get request and caching
        # repsonse
        response.raise_for_status()  # Raise an exception for error status codes (important we don't handle as they
        # rate limit API)
        odds_data = response.json()  # Get Response's json containing odds data

        return odds_data
