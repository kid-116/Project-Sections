from django.contrib import admin
from . import models


class OrganisationAdmin(admin.ModelAdmin):
    search_fields = [
        'name',
    ]
    list_display = [
        'name',
        'administrator',
        'is_activated',
    ]
    fields = [
        'name',
        'administrator',
        'is_activated',
    ]
    readonly_fields = [
        'name',
        'administrator', 
    ]

admin.site.register(models.Organisation, OrganisationAdmin)
