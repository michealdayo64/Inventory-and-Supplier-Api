from django.urls import path
from .views import ListOfItemsByASupplier, ViewAllItem, AddItem, UpdateItem, RemoveItem

urlpatterns = [
    path('supplier-list-items/<id>/', ListOfItemsByASupplier.as_view()),
    path('view-all-items/', ViewAllItem.as_view()),
    path('add_item/', AddItem.as_view()),
    path('update_item/<id>/', UpdateItem.as_view()),
    path('remove_item/<id>/', RemoveItem.as_view())
]
