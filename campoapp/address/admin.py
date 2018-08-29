from django.contrib import admin
from .models import State,Municipality,Location,Address

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name','short_name',)

@admin.register(Municipality)
class MunicipalityAdmin(admin.ModelAdmin):
    list_display = ('id','name',)
    list_filter = ('state__short_name',)

    ordering = ['id']

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name','municipality')
    list_filter = ('municipality__state__short_name',)    
    search_fields = ['name','municipality__name']

    ordering = ['municipality','name']


