from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

# Supplier Record Table

class SupplierRecord(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(12)], blank=True, null=True)
    address = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'