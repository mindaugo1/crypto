from django.db import models


# ID automatiskai
# open/high/open/close fieldas valiutai
# indexing table columns for faster perfomance timestamp/currency
# crypto one to many
class Crypto(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=500)


class Detail(models.Model):
    id = models.IntegerField(primary_key=True)
    time_stamp = models.CharField(max_length=500)
    open = models.CharField(max_length=500)
    high = models.CharField(max_length=500)
    low = models.CharField(max_length=500)
    close = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    models.ForeignKey(Crypto, on_delete=models.CASCADE)

    def __str__(self):
        return f'ID: {self.id}, Time stamp: {self.time_stamp}, Open: {self.open}, High: {self.high}, Low: {self.low}, Close: {self.close}'
