def calculate_risk_score(df):
    risk_score = 0
    flags = []

    tx_count = len(df)
    zero_value_txs = len(df[df["value_eth"] == 0])
    high_value_txs = len(df[df["value_eth"] > 100])

    if tx_count > 5000:
        risk_score += 30
        flags.append("High transaction volume")

    if zero_value_txs > 100:
        risk_score += 20
        flags.append("Many zero-value transactions")

    if high_value_txs > 5:
        risk_score += 40
        flags.append("High-value transfers detected")

    if risk_score == 0:
        flags.append("No obvious suspicious patterns")

    return risk_score, flags
