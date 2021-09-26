from pycoingecko import CoinGeckoAPI
import pandas as pd
cg = CoinGeckoAPI()

# def all_currency_by_markets():
    
#     coin_market = cg.get_coins_markets(vs_currency = "usd")
#     df_market = pd.DataFrame(coin_market, columns = ['market_cap_rank', 'id', 'current_price', 'market_cap'])
#     df_market.set_index('market_cap_rank', inplace=True)
#     print(df_market)

def n_currency_by_markets(n):
    coin_market = cg.get_coins_markets(vs_currency = "usd", per_page = n)
    df_market = pd.DataFrame(coin_market, columns = ['market_cap_rank', 'id', 'current_price', 'market_cap'])
    df_market.set_index('market_cap_rank', inplace=True)
    print(df_market)

if __name__ == "__main__":
    while(True):
        print("Welcome to crypto listings app. Choose the function below: ")
        print("Choose the amount of cryptocurrencies to be shown by market capitalization.")
        print("0. To exit.")
        a = input()
        if a == "0":
            exit()
        else:
            n_currency_by_markets(a)

