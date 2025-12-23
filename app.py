from flask import Flask, render_template, request
from etherscan_api import get_wallet_transactions
from analyzer import analyze_transactions
from graph import generate_spider_map
from report import generate_wallet_report
from risk import calculate_risk_score

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    data = None
    risk_score = None
    flags = []

    if request.method == "POST":
        wallet = request.form["wallet"].strip()

        if wallet.startswith("0x") and len(wallet) == 42:
            txs = get_wallet_transactions(wallet)
            df = analyze_transactions(txs)

            if not df.empty:
                generate_spider_map(df)
                generate_wallet_report(df)
                risk_score, flags = calculate_risk_score(df)

                data = df.head(50).to_dict(orient="records")

    return render_template(
        "index.html",
        data=data,
        risk_score=risk_score,
        flags=flags
    )

if __name__ == "__main__":
    app.run(debug=True)
