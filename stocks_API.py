import requests
import os
import pandas as pd

api_key = os.getenv('CNODG5LTW3G2W1Z4')
base_url = 'https://www.alphavantage.co/query?'
function = 'TIME_SERIES_DAILY'
symbol = 'AAPL'
outputsize = 'full'
datatype='csv'

response = requests.get(f'{base_url}function={function}&symbol={symbol}&outputsize={outputsize}&datatype={datatype}&apikey={api_key}')
with open('AAPL.csv', 'wb') as file:
    file.write(response.content)

df = pd.read_csv('AAPL.csv') #Create pandas dataframe

df.set_index('timestamp', inplace=True) #Time-series index
print(df)