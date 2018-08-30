# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import State, Municipality, Location, Address

class StateResource(resources.ModelResource):

    class Meta:
        model = State
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ['id', ]
        exclude = ('id',)
        fields = ('name', 'short_name',)

    def get_instance(self, instance_loader, row):
        try:
            params = {}
            for key in instance_loader.resource.get_import_id_fields():
                field = instance_loader.resource.fields[key]
                params[field.attribute] = field.clean(row)
            return self.get_queryset().get(**params)
        except Exception:
            return None

class MunicipalityResource(resources.ModelResource):

    class Meta:
        model = Municipality
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ['id', ]
        exclude = ('id',)
        fields = ('state', 'name',)

    def get_instance(self, instance_loader, row):
        try:
            params = {}
            for key in instance_loader.resource.get_import_id_fields():
                field = instance_loader.resource.fields[key]
                params[field.attribute] = field.clean(row)
            return self.get_queryset().get(**params)
        except Exception:
            return None

class LocationResource(resources.ModelResource):

    class Meta:
        model = Location
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ['id', ]
        exclude = ('id',)
        fields = ('municipality', 'name',)

    def get_instance(self, instance_loader, row):
        try:
            params = {}
            for key in instance_loader.resource.get_import_id_fields():
                field = instance_loader.resource.fields[key]
                params[field.attribute] = field.clean(row)
            return self.get_queryset().get(**params)
        except Exception:
            return None            

@admin.register(State)
class StateAdmin(ImportExportModelAdmin):
    list_display = ('id','name', 'short_name',)
    resource_class = StateResource


@admin.register(Municipality)
class MunicipalityAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ('state__short_name',)
    resource_class = MunicipalityResource

    ordering = ['id']


@admin.register(Location)
class LocationAdmin(ImportExportModelAdmin):
    list_display = ('name', 'municipality')
    list_filter = ('municipality__state__short_name',)
    search_fields = ['name', 'municipality__name']
    resource_class = LocationResource

    ordering = ['municipality', 'name']
