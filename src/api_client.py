import requests

class APIClient:
    @staticmethod
    def get_quote():
        try:
            response = requests.get("https://zenquotes.io/api/random")
            data = response.json()
            return data[0].get("q")
        except Exception:
            return "Keep going! You're doing great!"
