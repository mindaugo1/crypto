from django.db import models


# open/high/open/close fieldas valiutai
# indexing table columns for faster perfomance timestamp/currency
# crypto one to many


class Crypto(models.Model):
    CRYPTO_CHOICES = [
        ('BTC', 'Bitcoin'),
        ('ETH', 'Etherium'),
        ('SOL', 'Solana'),
    ]
    crypto = models.CharField(max_length=512, choices=CRYPTO_CHOICES, default='')

    def __str__(self):
        return f'Crypto Name: {self.crypto}'

    class Meta:
        ordering = ('pk',)
        verbose_name_plural = "Crypto"


class Detail(models.Model):
    time_stamp = models.CharField(max_length=500)
    open = models.DecimalField(max_digits=7, decimal_places=2)
    high = models.CharField(max_length=500)
    low = models.CharField(max_length=500)
    close = models.CharField(max_length=500)
    volume = models.CharField(max_length=500, null=True)
    market_cap = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    # currency_name = models.ForeignKey(Crypto, on_delete=models.CASCADE, default='')

    class Meta:
        ordering = ('pk',)
        indexes = [
            models.Index(fields=['time_stamp', 'open', 'high', 'low', 'close', 'volume', 'market_cap', 'created_at']),
        ]

    def __str__(self):
        return f'Time stamp: {self.time_stamp}, Open: {self.open}, High: {self.high}, ' \
               f'Low: {self.low}, Close: {self.close}, Volume: {self.volume}, Market_cap: {self.market_cap}'
