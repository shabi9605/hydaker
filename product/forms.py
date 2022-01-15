from django import forms
from django.db.models import fields
from .models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields = ('name','description')

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields = ('category','name','slug','photo','photo1','photo2','photo3','warrenty',
        'price','dimensions','stock','description','contact_number',
        'basic_color','materials','foam','wood_name','is_available','created')



class CustomizeForm(forms.ModelForm):
    class Meta:
        model=Customize
        fields=('wood','color','material','dimension','polish','foam','quantity')