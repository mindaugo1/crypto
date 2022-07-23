from django.core.management.base import BaseCommand
from main.strategy import get_moving_avarage, get_date_range
import subprocess

class Command(BaseCommand):

	def handle(self, **options):
		range_ = get_date_range()
		print("--------------")
		for date in range_:
			ma50 = get_moving_avarage(date=date, numdays=50, currency="EUR", crypto="BTC") 
			print(ma50)

