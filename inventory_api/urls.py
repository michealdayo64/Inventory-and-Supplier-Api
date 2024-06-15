from django.urls import path
from .views import ViewSuppliers, ListOfItemsByASupplier, ViewSuppliersForAnItem, AddItem

urlpatterns = [
    path('view_suppliers/', ViewSuppliers.as_view()),
    path('item_by_supplier/<id>/', ListOfItemsByASupplier.as_view()),
    path('view_suppliers_by_item/', ViewSuppliersForAnItem.as_view()),
    path('add_item/', AddItem.as_view())
]
