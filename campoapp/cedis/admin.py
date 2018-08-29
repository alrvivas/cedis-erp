from django.contrib import admin

from cedis.models import Cedis,CedisProduct,MixedProduct,Promotion,Route

class PromotionInline(admin.StackedInline):
    model = Promotion
    fields = ['isActive','name',('start_date','end_date'),('discount','condition'),'description']
    extra = 1

class ProductInline(admin.TabularInline):
    model = CedisProduct
    extra = 3

class MixedProductInline(admin.TabularInline):
    model = MixedProduct
    extra = 3

@admin.register(Cedis)
class CedisAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [ProductInline,MixedProductInline]
    prepopulated_fields = {'slug' : ('name',)}

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('name','cedis',)
    list_editable = ('cedis',)
    
    prepopulated_fields = {'slug' : ('name',)}


@admin.register(CedisProduct)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('get_name_cedis','stock','cedis',)
    list_filter = ('cedis',)    
    inlines = [PromotionInline]
    search_fields = ['product__name',]
    

@admin.register(MixedProduct)
class MixedProductAdmin(admin.ModelAdmin):
    list_display = ('get_name','stock','cedis',)
    list_filter = ('cedis',)

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('name',)