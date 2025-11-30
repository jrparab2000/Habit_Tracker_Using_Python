import requests
"""
APIClient Module 🚀
-----------------
This module defines the APIClient class, a utility class responsible for 
fetching external data. 

In this application, its primary function is to retrieve motivational quotes 
from a public API to encourage users.
"""
class APIClient:
    @staticmethod
    def get_quote():
        """
        Fetches a random motivational quote from the ZenQuotes API.
        
        It handles potential connection errors or API issues by providing a 
        default motivational message.
        
        Returns:
            str: A random motivational quote, or a default message if the API call fails.
        """
        try:
            response = requests.get("https://zenquotes.io/api/random")
            data = response.json()
            return data[0].get("q")
        except Exception:
            return "Keep going! You're doing great!"
