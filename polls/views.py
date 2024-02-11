# Create your views here.
from django.shortcuts import render
from .models import Item
from .forms import ItemForm


def item_list(request):
    form = ItemForm(request.GET)

    if form.is_valid():
        search_name = form.cleaned_data.get('search_name', '')
        items = Item.objects.filter(name__icontains=search_name)
    else:
        items = Item.objects.all()

    return render(request, 'item_list.html', {'items': items, 'form': form})
