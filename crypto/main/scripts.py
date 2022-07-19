import requests
import os
import pandas as pd
import csv
import argparse
from .models import Crypto, Detail

base_url = 'https://www.alphavantage.co/query?'
function = 'DIGITAL_CURRENCY_DAILY'

def get_raw_response(symbol, market, base_url=base_url, function=function):
    return requests.get(
        f'{base_url}function={function}&symbol={symbol}&market={market}&apikey={None}&datatype=csv')

def parse_response(response):
    csv_string = response.content.decode('utf-8')
    lines = csv_string.splitlines()
    reader = csv.reader(lines)
    return list(reader)
    
# def upload_to_database(data):
#     list_of_ds_objects = []
#     for row in data[1:]:
#         crypto_row = Detail(time_stamp=row[0], open=row[1], high=row[2], low=row[3], close=row[4], volume=row[5],
#                             market_cap=row[6], created_at=row[7])
#         crypto_row.save()

def run_script(symbol, market):
    response = get_raw_response(symbol, market)
    data = parse_response(response)

