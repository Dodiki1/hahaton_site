from django.urls import path
from .views import item_list

urlpatterns = [
    path('item-list/', item_list, name='item_list'),
    # Add other paths as needed
]
