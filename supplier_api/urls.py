from django.urls import path
from .views import ViewSuppliersForAnItem, AddSupplier, UpdateSupplier, AllSupplierList, DetailSupplier


# ALL ROUTING URL FOR SUPPLIER APP WHICH COMUNICATES WITH THE VIEWS

urlpatterns = [
    path('view-suppliers-item/', ViewSuppliersForAnItem.as_view()),
    path('add-supplier/', AddSupplier.as_view()),
    path('update-supplier/<id>/', UpdateSupplier.as_view()),
    path('all-supplier-list/', AllSupplierList.as_view()),
    path('supplier-detail/<id>/', DetailSupplier.as_view()),
]
