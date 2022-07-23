from django.core.management.base import BaseCommand
from ...strategy import get_moving_avarege, get_date_range
import subprocess
import seaborn as sns
import pandas as pd
import numpy as np

class Command(BaseCommand):

	def handle(self, **options):
		date_range = get_date_range(numdays=10)	
		ma50_list = []
		ma200_list = []
		for day in date_range:
			ma = get_moving_avarege(date=day, numdays=50, crypto="BTC", currency="EUR")
			ma200 = get_moving_avarege(date=day, numdays=50, crypto="BTC", currency="EUR")	
			ma50_list.append(ma)
			ma200_list.append(ma200)

		
		data = {"day": date_range, "ma50": ma50_list, "ma200": ma200_list}
		

		hi = pd.DataFrame(data)
		print(hi)
		sns.set(style='whitegrid')
		 
		plottt = sns.scatterplot(x="day", y="ma50", data=hi)
		plottt.figure.savefig("./fadfasdfadsf.jpg")

