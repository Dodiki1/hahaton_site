from django.urls import path
from .views import item_list
from .views import yyyy_view


urlpatterns = [
    path('item-list/', item_list, name='item_list'),
    path('yyyy/', yyyy_view, name='yyyy'),
    # Add other paths as needed
]
