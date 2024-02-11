from django.urls import path
from .views import item_list
from .views import index_view

urlpatterns = [
    path('item-list/', item_list, name='item_list'),
    path('index/', index_view, name='index'),
    # Add other paths as needed
]
