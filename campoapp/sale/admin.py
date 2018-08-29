from django.contrib import admin

from .models import Payment_Status,Shipping_Status,Payment_Type,Order,Deposit_Balance

@admin.register(Payment_Status)
class Payment_StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
    prepopulated_fields = {'slug' : ('name',)}

@admin.register(Shipping_Status)
class Shipping_StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
    prepopulated_fields = {'slug' : ('name',)}


@admin.register(Deposit_Balance)
class Deposit_BalanceAdmin(admin.ModelAdmin):
    list_display = ('order','deposit',)
    