from datetime import datetime, timedelta
from decimal import Decimal

from .models import Detail, Crypto

def get_date_range(numdays=30):
    date_now = datetime.now()
    days = [date_now - timedelta(days=day)  for day in range(numdays)] 
    days_string = [date.strftime("%Y-%m-%d") for date in sorted(days)]
    return days_string



def get_moving_avarage(start_date, days, crypto, currency):
    date_start = datetime.strptime(start_date, "%Y-%m-%d") - timedelta(days=days)

    crypto = Crypto.objects.filter(crypto=crypto).first()
    close_prices = list(
        Detail.objects.filter(
            currency_name_id=crypto.id, currency=currency, time_stamp__gte=date_start
        ).values("close")
    )

    ma = sum([Decimal(row.get("close")) for row in close_prices]) / len(close_prices)
    return ma
