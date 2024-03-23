import alpaca_trade_api as alpaca
import os
from dotenv import load_dotenv
import polygon

class AlpacaCommunicator:
    def __init__(self, pub_key, sec_key, base_url):
        self.alpaca_api = alpaca.REST(key_id=pub_key, secret_key=sec_key, base_url=base_url)
    def market_buy(self, ticker, quantity=1):
        self.alpaca_api.submit_order(  
            symbol=ticker,
            qty=quantity,
            side="buy",
            type='market',
            time_in_force='gtc'
        )

    def limit_buy(self, ticker, quantity=1, limit_price=1):
        self.alpaca_api.submit_order(
            symbol=ticker,
            qty=quantity,
            side="buy",
            type='limit',
            time_in_force='gtc',
            limit_price=limit_price
        )

    def get_stock_price(self, ticker):
        return self.alpaca_api.get_latest_quote(ticker).ap

    def get_account(self):
        return self.alpaca_api.get_account()
    
    def get_positions(self):
        return self.alpaca_api.list_positions()    
        