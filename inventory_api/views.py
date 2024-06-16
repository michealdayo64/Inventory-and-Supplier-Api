from django.shortcuts import render
from rest_framework.views import APIView  # type: ignore
from rest_framework.permissions import AllowAny, IsAuthenticated  # type: ignore
from rest_framework.response import Response  # type: ignore
from rest_framework import status  # type: ignore
from rest_framework.authtoken.models import Token  # type: ignore
from inventory_api.models import ItemsRecord
from supplier_api.models import SupplierRecord
from inventory_api.serializers import ItemSerializer, UserSerializer

# Create your views here.


# API VIEW TO CREATE EMPLOYEE ACCOUNT

class UserCreate(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        payload = {}
        if request.method == "POST":
            user_data = UserSerializer(data=request.data or None)
            if user_data.is_valid():
                user = user_data.save()
                user.set_password(user.password)
                user.save()

                # CREATE TOKEN
                Token.objects.create(user=user)

                payload['msg'] = "Register Successfully"
                return Response(data=payload, status=status.HTTP_201_CREATED)
            else:
                payload['msg'] = "Invalid Data"
                return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
        else:
            payload['msg'] = 'Invalid Request'
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)


# API VIEW FOR EMPLOYEE TO SEE LIST OF ITEMS SUPPLIED BY A SUPPLIER
class ListOfItemsByASupplier(APIView):
    permission_classes = (IsAuthenticated, )

    def put(self, request, id):
        payload = {}
        if request.method == 'PUT':
            supplier_id = SupplierRecord.objects.get(id=id)
            items = ItemsRecord.objects.filter(supplier=supplier_id)
            item_serializer = ItemSerializer(items, many=True)
            if item_serializer:
                payload = {
                    "msg": item_serializer.data
                }
                return Response(data=payload, status=status.HTTP_200_OK)
            else:
                payload = {
                    "msg": "Data not found"
                }
                return Response(data=payload, status=status.HTTP_200_OK)
        else:
            payload = {
                'msg': "Invalid Request"
            }
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)


# API VIEW FOR EMPLOYEE TO VIEW ALL ITEM IN THE STORE
class ViewAllItem(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        payload = {}
        if request.method == 'GET':
            items = ItemsRecord.objects.all()
            serializer = ItemSerializer(items, many=True)
            payload = {
                'msg': serializer.data
            }
            return Response(data=payload, status=status.HTTP_200_OK)
        else:
            payload = {
                "msg": "Invalid Request"
            }
            return Response(data=payload, status=status.HTTP_401_BAD_REQUEST)


# API VIEW TO ADD ITEM TO THE STORE
class AddItem(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        payload = {}
        if request.method == 'POST':
            serializer = ItemSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                payload = {
                    'msg': "Item Saved Successfully",
                    "data": serializer.data
                }
                return Response(data=payload, status=status.HTTP_201_CREATED)
        else:
            payload = {
                'msg': "Invalid Request"
            }
            return Response(data=payload, status=status.HTTP_401_BAD_REQUEST)


# API VIEW TO UPDATE ITEM IN THE STORE
class UpdateItem(APIView):
    permission_classes = (AllowAny, )

    def put(self, request, id):
        payload = {}
        if request.method == "PUT":
            item_id = ItemsRecord.objects.get(id=id)
            serializer = ItemSerializer(data=request.data, instance=item_id)
            if serializer.is_valid():
                serializer.save()
            payload = {
                "msg": "Item Updated Successfully",
                'data': serializer.data
            }
            return Response(data=payload, status=status.HTTP_200_OK)
        else:
            payload = {
                'msg': "Invalid Request"
            }
            return Response(data=payload, status=status.HTTP_401_BAD_REQUEST)


# API  VIEW TO REMOVE ITEM FROM THE STORE
class RemoveItem(APIView):
    permission_classes = (AllowAny, )

    def delete(self, request, id):
        payload = {}
        if request.method == 'DELETE':
            item_id = ItemsRecord.objects.get(id=id)
            item_id.delete()
            payload = {
                "msg": "Item Removed Successfully"
            }
            return Response(data=payload, status=status.HTTP_200_OK)
        else:
            payload = {
                'msg': 'Invalid Request'
            }
            return Response(data=payload, status=status.HTTP_401_BAD_REQUEST)
