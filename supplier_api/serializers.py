from rest_framework import serializers  # type: ignore
from .models import SupplierRecord


# SERIALIZER FOR SUPPLIER
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierRecord
        fields = ('pk', 'name', 'email', 'phone_number',
                  'address', 'date_created', 'date_updated', )
