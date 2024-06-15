from django.urls import path
from .views import ViewSuppliersForAnItem

urlpatterns = [
    path('view-suppliers-item/', ViewSuppliersForAnItem.as_view())
]