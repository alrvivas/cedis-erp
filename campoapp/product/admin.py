# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from import_export import resources
from import_export.fields import Field
from import_export.admin import ImportExportModelAdmin
from product.models import Category, Product,MixedProduct,MProducts


class ProductResource(resources.ModelResource):

    barcode = Field(attribute='barcode', saves_null_values=True)

    class Meta:
        model = Product
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ['id','barcode',]
        exclude = ('id',)
        #saves_null_values = ('barcode',)
        fields = ('name','barcode','standard_price','weight','unit','category')

    def get_instance(self, instance_loader, row):
        try:
            params = {}
            for key in instance_loader.resource.get_import_id_fields():
                field = instance_loader.resource.fields[key]
                params[field.attribute] = field.clean(row)
            return self.get_queryset().get(**params)
        except Exception:
            return None


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','orden')
    ordering = ('orden',)
    
    prepopulated_fields = {'slug' : ('name',)}

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('name','category','standard_price','weight','unit') 
    list_editable = ('category','standard_price')   
    search_fields = ['name',]
    resource_class = ProductResource
    prepopulated_fields = {'slug' : ('name',)}
    ordering = ('category','weight',)


class MixedProductInline(admin.TabularInline):
    model = MProducts
    extra = 3

@admin.register(MixedProduct)
class MixedProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [MixedProductInline]

    prepopulated_fields = {'slug' : ('name',)}




