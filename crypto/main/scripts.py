import requests
import os
import pandas as pd
import csv
from crypto.main.models import Detail

api_key = os.getenv('CNODG5LTW3G2W1Z4')
base_url = 'https://www.alphavantage.co/query?'
function = 'DIGITAL_CURRENCY_DAILY'
symbol = 'BTC'
outputsize = 'full'
market = 'USD'
datatype = 'csv'
response = requests.get(
    f'{base_url}function={function}&symbol={symbol}&market={market}&apikey={api_key}&datatype={datatype}')
# print(response.content)
# print(response.json())

csv_string = response.content.decode('utf-8')
# print(csv_string)
lines = csv_string.splitlines()
reader = csv.reader(lines)
parsed_csv = list(reader)
reader = csv.reader(lines)
parsed_data = list(reader)

list_of_ds_objects = []
for row in parsed_data[1:]:
    crypto_row = Detail(time_stamp=row[0] , open=row[1], high=row[2], low=row[3], close=row[4], volume=row[5], market_up=row[6], created_cap=row[7], currency_name=1)
    crypto_row.save()
    


# print(parsed_csv)

# with open('BTC.csv', 'wb') as file:
#     file.write(response.content)
# df = pd.read_csv('BTC.csv')  # Create pandas dataframe
#
# df.set_index('timestamp', inplace=True)  # Time-series index
# print(df)
