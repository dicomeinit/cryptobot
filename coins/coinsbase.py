import requests
import pandas as pd

API_KEY = '6PQGCTR965JFFEAO'
symbol = 'ETH'
interval_var = '5min'

url = 'https://www.alphavantage.co/query?function=CRYPTO_INTRADAY&symbol='+symbol+'&market=USD&interval='+interval_var+'&apikey='+API_KEY+'&datatype=csv&outputsize=full'

df = pd.read_csv(url)
df = df[::-1].reset_index()
df = df.drop(['index'], axis=1)

print(df)
