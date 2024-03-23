import alpaca_trade_api as tradeapi

SEC_KEY = 'vwcYuiKFAbvs3Jz7ZA43j8ZFJPNT7MTvXQFEiuWX' # Enter Your Secret Key Here
PUB_KEY = 'PKWS1ENRD06Q8SXH2PBA' # Enter Your Public Key Here
BASE_URL = 'https://paper-api.alpaca.markets' # This is the base URL for paper trading
api = tradeapi.REST(key_id= PUB_KEY, secret_key=SEC_KEY, base_url=BASE_URL) # For real trading, don't enter a base_url

while True:
    valid = True
    ticker = input("Enter the ticker of the stock you want to buy: ")
    action = input("Buy or sell?: ")
    if ticker == "":
        print("Please enter a valid ticker")
        valid = False
    if action != "buy" and action != "sell":
        print("Please enter a valid action")
        valid = False
    # Buy a stock
    if valid == True:
        confirm = input(f"You chose to {action} 1 share of {ticker}, confirm? y/N: ")

        if confirm.lower() == 'y':  
            api.submit_order(
            symbol=ticker, # Replace with the ticker of the stock you want to buy
            qty=1,
            side=action,
            type='market', 
            time_in_force='gtc' # Good 'til cancelled
            )
        else:
            print("Order cancelled")