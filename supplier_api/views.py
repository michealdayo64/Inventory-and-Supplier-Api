from django.shortcuts import render
from rest_framework.views import APIView  # type: ignore
from rest_framework.permissions import AllowAny, IsAuthenticated  # type: ignore
from rest_framework.response import Response  # type: ignore
from rest_framework import status  # type: ignore
from inventory_api.models import ItemsRecord
from inventory_api.serializers import SuppliersOfAnItemSerializer
from supplier_api.models import SupplierRecord
from .serializers import SupplierSerializer


# API VIEW FOR EMPLOYEE TO VIEW ALL SUPPLIERS FOR A PARTICULER ITEM

class ViewSuppliersForAnItem(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        payload = {}
        if request.method == "POST":
            item = request.data.get('item')
            print(item)
            get_item = ItemsRecord.objects.filter(name=item)
            print(get_item)
            if len(get_item) > 0:
                serial_data = SuppliersOfAnItemSerializer(get_item, many=True)
                if serial_data:
                    payload = {
                        'msg': 'Success',
                        'data': serial_data.data
                    }
                    return Response(data=payload, status=status.HTTP_200_OK)
                else:
                    payload = {
                        'msg': "No data found"
                    }
                    return Response(data=payload, status=status.HTTP_200_OK)
            else:
                payload = {
                    'msg': "No data found"
                }
                return Response(data=payload, status=status.HTTP_200_OK)
        else:
            payload = {
                'msg': 'Invalid Request'
            }
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)


# API VIEW TO ADD SUPPLIER


class AddSupplier(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        payload = {}
        if request.method == 'POST':
            serializer = SupplierSerializer(data=request.data or None)
            if serializer.is_valid():
                serializer.save()
                payload = {
                    'msg': "Success",
                    'data': serializer.data
                }
                return Response(data=payload, status=status.HTTP_201_CREATED)
        else:
            payload = {
                'msg': "invalid Request"
            }
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)


# API VIEW TO UPDATE SUPPLIER INFO


class UpdateSupplier(APIView):
    permission_classes = (IsAuthenticated, )

    def put(self, request, id):
        if request.method == 'PUT':
            payload = {}
            supplier_id = SupplierRecord.objects.get(id=id)
            serializer = SupplierSerializer(
                data=request.data, instance=supplier_id)
            if serializer.is_valid():
                serializer.save()
                payload = {
                    "msg": "Success",
                    'data': serializer.data
                }
                return Response(data=payload, status=status.HTTP_200_OK)
            else:
                payload = {
                    'msg': "Invalid Data"
                }
                return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
        else:
            payload = {
                'msg': "Invalid Request"
            }
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)


# API VIEW TO DISPLAY LIST OF ALL SUPPLIER


class AllSupplierList(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        payload = {}
        if request.method == 'GET':
            supplier_list = SupplierRecord.objects.all()
            if len(supplier_list) > 0:
                serializer = SupplierSerializer(supplier_list, many=True)
                if serializer:
                    payload = {
                        'msg': 'Success',
                        'data': serializer.data
                    }
                    return Response(data=payload, status=status.HTTP_200_OK)
                else:
                    payload = {
                        'msg': 'Invalid Request'
                    }
                    return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
            else:
                payload = {
                    'msg': 'No data Found'
                }
                return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
        else:
            payload = {
                'msg': 'Invalid Request'
            }
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)


# API VIEW FOR SUPPLIER DETAIL INFORMATION


class DetailSupplier(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, id):
        if request.method == 'GET':
            payload = {}
            supplier_id = SupplierRecord.objects.get(id=id)
            serializer = SupplierSerializer(
                instance=supplier_id)
            payload = {
                "msg": 'Success',
                'data': serializer.data
            }
            return Response(data=payload, status=status.HTTP_200_OK)

        else:
            payload = {
                'msg': "Invalid Request"
            }
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
