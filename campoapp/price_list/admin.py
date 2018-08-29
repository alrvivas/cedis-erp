from django.contrib import admin
from django.forms.models import BaseInlineFormSet
from .models import PriceList,ProductList,MixedProductList
from .forms import ProductForm


class ProductInline(admin.TabularInline):
    model = ProductList
    form = ProductForm
    autocomplete_fields = ['product',]
    extra = 3

    
class MixedProductInline(admin.TabularInline):
    model = MixedProductList
    extra = 3

@admin.register(PriceList)
class PriceListAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [ProductInline,MixedProductInline]
    prepopulated_fields = {'slug' : ('name',)}

@admin.register(ProductList)
class ProductListAdmin(admin.ModelAdmin):
	list_display = ('product','price','price_list',)
	list_filter = ('price_list',)
		