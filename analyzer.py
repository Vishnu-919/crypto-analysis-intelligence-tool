import pandas as pd
from datetime import datetime

def analyze_transactions(transactions):
    if not transactions:
        print("No transactions to analyze.")
        return pd.DataFrame()

    rows = []

    for tx in transactions:
        rows.append({
            "txid": tx.get("hash"),
            "from": tx.get("from"),
            "to": tx.get("to"),
            "value_eth": int(tx.get("value", 0)) / 1e18,
            "timestamp": datetime.utcfromtimestamp(int(tx.get("timeStamp"))),
            "direction": "OUT" if tx.get("from") else "IN"
        })

    return pd.DataFrame(rows)
