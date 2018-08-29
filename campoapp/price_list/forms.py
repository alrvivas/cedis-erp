from django import forms
from .models import ProductList,PriceList
from cedis.models import CedisProduct

class ProductForm(forms.ModelForm):	
	class Meta:
		model = ProductList
		fields = ('__all__')