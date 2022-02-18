from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
import pandas as pd
import json

def fetch_data():
    A = cg.get_coin_market_chart_by_id(id = 'bitcoin', vs_currency = 'usd', days = '5', interval = 'daily')
    B = cg.get_coin_market_chart_by_id(id = 'algorand', vs_currency = 'usd', days = '5', interval = 'daily')
    C = cg.get_coin_market_chart_by_id(id = 'ethereum', vs_currency = 'usd', days = '5', interval = 'daily')
    D = cg.get_coin_market_chart_by_id(id = 'solana', vs_currency = 'usd', days = '5', interval = 'daily')
    Bitcoin_data = json.dumps(A)
    Algorand_data = json.dumps(B)
    Ethereum_data = json.dumps(C)
    Solana_data = json.dumps(D)
    Bitcoin_File = open("bitcoin.json", "w")
    Bitcoin_File.write(Bitcoin_data)
    Bitcoin_File.close()
    Algorand_File = open("algorand.json", "w")
    Algorand_File.write(Algorand_data)
    Algorand_File.close()
    Ethereum_File = open("ethereum.json", "w")
    Ethereum_File.write(Ethereum_data)
    Ethereum_File.close()
    Solana_File = open("solana.json", "w")
    Solana_File.write(Solana_data)
    Solana_File.close()

