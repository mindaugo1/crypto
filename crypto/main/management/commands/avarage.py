from django.core.management.base import BaseCommand
from main.strategy import get_moving_avarage
import subprocess

class Command(BaseCommand):

	def handle(self, **options):
		print("--------------")
		for date in ["2022-06-01", "2022-06-02", "2022-06-03", "2022-06-04"]:
			ma50 = get_moving_avarage(start_date=date, days=50, currency="EUR", crypto="BTC") 
			print(ma50)

