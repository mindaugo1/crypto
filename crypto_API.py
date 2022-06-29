import requests
import os
import pandas as pd

api_key = os.getenv('CNODG5LTW3G2W1Z4')
base_url = 'https://www.alphavantage.co/query?'
function = 'DIGITAL_CURRENCY_DAILY'
symbol = 'BTC'
outputsize = 'full'
market = 'USD'
datatype='csv'

response = requests.get(f'{base_url}function={function}&symbol={symbol}&market={market}&apikey={api_key}&datatype={datatype}')
with open('BTC.csv', 'wb') as file:
    file.write(response.content)

df = pd.read_csv('BTC.csv') #Create pandas dataframe

df.set_index('timestamp', inplace=True) #Time-series index
print(df)