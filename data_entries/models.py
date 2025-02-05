from django.db import models
from clients.models import Client
from currencies.models import Currency

class DataEntry(models.Model):
    TRANSACTION_TYPES = (
        ('income', 'Income'),
        ('expense', 'Expense'),
    )

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    currency_in = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='currency_in')
    currency_out = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='currency_out')
    transaction_type = models.CharField(max_length=7, choices=TRANSACTION_TYPES)
    amount_in = models.DecimalField(max_digits=10, decimal_places=2)
    amount_out = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cross_rate = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        #self.cross_rate = get_exchange_rate(self.currency_in.code if "USDT" in self.currency_out.code else self.currency_out.code)
        try:
            self.cross_rate = self.amount_in/self.amount_out
        except Exception as e:
            self.cross_rate = 0
        super(DataEntry, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.client} - {self.currency_in}/{self.currency_out} - {self.transaction_type} - {self.amount_in} - {self.amount_out}"