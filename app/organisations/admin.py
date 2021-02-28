from django.contrib import admin
from . import models


class OrganisationAdmin(admin.ModelAdmin):
    search_fields = [
        'name',
    ]
    list_display = [
        'name',
        'is_activated',
    ]
    fields = [
        'name',
        'is_activated',
    ]
    readonly_fields = [
        'name',
    ]

admin.site.register(models.Organisation, OrganisationAdmin)
