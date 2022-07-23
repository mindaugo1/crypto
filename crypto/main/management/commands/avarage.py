from django.core.management.base import BaseCommand
from ...strategy import get_moving_avarege, get_date_range
import subprocess
import seaborn as sns
import pandas as pd
import numpy as np

class Command(BaseCommand):

	def handle(self, **options):
		date_range = get_date_range(numdays=10)	
		list_of_moving_average = []
		for day in date_range:
			ma = get_moving_avarege(date=day, numdays=50, crypto="BTC", currency="EUR")
			list_of_moving_average.append(ma)
		
		data = {"day": date_range, "ma": list_of_moving_average}

		hi = pd.DataFrame(data)
		sns.set(style='whitegrid')
		 
		plottt = sns.scatterplot(x="day", y="ma", data=hi)
		plottt.figure.savefig("./fadfasdfadsf.jpg")

