import alpaca_trade_api as alpaca
import os
from dotenv import load_dotenv

load_dotenv()

PUBKEY = os.getenv("PUBKEY")
SECKEY = os.getenv("SECKEY")
BASEURL = os.getenv("BASEURL")

class AlpacaCommunicator:
    def __init__(self, pub_key, sec_key, base_url):
        self.api = alpaca.REST(key_id=pub_key, secret_key=sec_key, base_url=base_url)

    def submit_order(self, ticker, action):
        self.api.submit_order(  
            symbol=ticker,
            qty=1,
            side=action,
            type='market',
            time_in_force='gtc'
        )

    def get_account(self):
        return self.api.get_account()