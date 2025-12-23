# Crypto Analysis & Intelligence Mapping Tool

## Overview
A blockchain forensic tool designed to trace Ethereum transactions, visualize wallet relationships using spider maps, and generate investigation-ready reports for law enforcement agencies.

## Features
- Ethereum transaction tracing (Etherscan API v2)
- Wallet-to-wallet spider map visualization
- Wallet history CSV reports
- Risk scoring & suspicious pattern detection
- Web-based dashboard (Flask)

## Tech Stack
- Python
- Flask
- Etherscan API
- Pandas
- NetworkX
- Matplotlib

## How to Run
```bash
git clone https://github.com/YOUR_USERNAME/crypto-analysis-intelligence-tool.git
cd crypto-analysis-intelligence-tool
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
