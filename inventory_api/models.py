from django.db import models
# from django.contrib.auth.models import User
from supplier_api.models import SupplierRecord

# Create your models here.


# ITEM RECORD TABLE

class ItemsRecord(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(max_length=30, null=True, blank=True)
    supplier = models.ForeignKey(
        SupplierRecord, null=True, blank=True, related_name='supplier', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.supplier} supply {self.name}'
