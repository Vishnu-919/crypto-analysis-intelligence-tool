import requests
from config import ETHERSCAN_API_KEY, BASE_URL, CHAIN_ID

def get_wallet_transactions(address):
    params = {
        "chainid": CHAIN_ID,
        "module": "account",
        "action": "txlist",
        "address": address,
        "startblock": 0,
        "endblock": 99999999,
        "sort": "asc",
        "apikey": ETHERSCAN_API_KEY
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data.get("status") != "1":
        print("Etherscan Error:", data.get("message"))
        print("Details:", data.get("result"))
        return []

    return data["result"]
