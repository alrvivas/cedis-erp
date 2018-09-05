# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from import_export import resources
from import_export.fields import Field
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from django.forms.models import BaseInlineFormSet
from .models import Employee, Client
from address.models import Address


class ClientResource(resources.ModelResource):

    address = Field(column_name='name', attribute='Address',
                    widget=ForeignKeyWidget(Address, 'name'))

    class Meta:
        model = Client
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ['id', ]
        exclude = ('id',)
        fields = ('name', 'manager', 'rfc', 'call_visit', 'billing_condition',
                  'route', 'employee', 'tel_1', 'tel_2', 'cel', 'email',)

    def get_instance(self, instance_loader, row):
        try:
            params = {}
            for key in instance_loader.resource.get_import_id_fields():
                field = instance_loader.resource.fields[key]
                params[field.attribute] = field.clean(row)
            return self.get_queryset().get(**params)
        except Exception:
            return None


class ClientAdressInline(admin.TabularInline):
    model = Address
    fields = ['name', ('street', 'zip_code',) , 'location']
    autocomplete_fields = ['location', ]
    extra = 1


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'cedis',)

    prepopulated_fields = {'slug': ('name',)}


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'route')
    
    #list_editable = ('employee',)
    resource_class = ClientResource
    list_filter = ('route__cedis', 'price_list', 'route')
    fields = ('name', 'slug','manager', 'rfc', 'call_visit', 'employee', 'route', 'price_list', 'billing_condition', 'tel_1', 'tel_2', 'cel', 'email')    
    inlines = [ClientAdressInline]
    prepopulated_fields = {'slug': ('name',)}

    def get_cedis(self, obj):
        return obj.employee.cedis
    get_cedis.short_description = 'Cedis'
    get_cedis.admin_order_field = 'employee__cedis'