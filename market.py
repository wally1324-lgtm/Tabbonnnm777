import requests

class Market:
    def __init__(self):
        self.coins = [
            "bitcoin",
            "ethereum",
            "solana",
            "ripple",
            "binancecoin"
        ]

    def tick(self):
        url = (
            "https://api.coingecko.com/api/v3/simple/price"
            "?ids=bitcoin,ethereum,solana,ripple,binancecoin"
            "&vs_currencies=eur"
        )

        data = requests.get(url, timeout=10).json()

        prices = {
            "BTC": data["bitcoin"]["eur"],
            "ETH": data["ethereum"]["eur"],
            "SOL": data["solana"]["eur"],
            "XRP": data["ripple"]["eur"],
            "BNB": data["binancecoin"]["eur"]
        }

        return prices
