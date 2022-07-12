from django.db import models


# ID automatiskai - istryniau field, nes id sugeneruoja automatiskai django
# open/high/open/close fieldas valiutai
# indexing table columns for faster perfomance timestamp/currency
# crypto one to many

class MyModelManager(models.Manager):
    def update_id(self):
        for instance in self.all():
            instance.id = instance.get_index()
            instance.save()


class Crypto(models.Model):
    name = models.CharField(max_length=500)

    objects = MyModelManager()

    class Meta:
        ordering = ('pk',)
        verbose_name_plural = "Crypto"


class Detail(models.Model):
    time_stamp = models.CharField(max_length=500)
    open = models.DecimalField(max_digits=7, decimal_places=2)
    high = models.CharField(max_length=500)
    low = models.CharField(max_length=500)
    close = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    currency_name = models.ForeignKey(Crypto, on_delete=models.CASCADE, null=True)

    objects = MyModelManager()

    class Meta:
        ordering = ('pk',)
        indexes = [
            models.Index(fields=['time_stamp', 'open', 'high', 'low', 'close', 'created_at']),
        ]

    def __str__(self):
        return f'ID: {self.pk}, Time stamp: {self.time_stamp}, Open: {self.open}, High: {self.high}, ' \
               f'Low: {self.low}, Close: {self.close}'
