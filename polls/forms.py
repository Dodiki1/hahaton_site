from django import forms


class ItemForm(forms.Form):
    search_name = forms.CharField(label='Search by Name', max_length=100, required=False)
