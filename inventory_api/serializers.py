from rest_framework import serializers  # type: ignore
from .models import ItemsRecord
from supplier_api.serializers import SupplierSerializer
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
        )
        extra_kwargs = {'password': {'write_only': True}}


# SERIALIZER FOR ITEMS

class ItemSerializer(serializers.ModelSerializer):
    supplier = serializers.StringRelatedField(many=False)

    class Meta:
        model = ItemsRecord
        fields = ('pk', 'name', 'description', 'price', 'supplier',
                  'date_created', 'date_updated', )


# SERIALIZER FOR SUPPLIERS OF A SPECIFIC ITEM
class SuppliersOfAnItemSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer(many=False)

    class Meta:
        model = ItemsRecord
        fields = ('supplier', )
