from django.contrib import admin
from .models import Bracket, JoinRequest
from django.db import models
from django import forms
from accounts.models import Account


class BracketAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': forms.CheckboxSelectMultiple},
    }
    search_fields = [
        'name',
        'graduation_year',
    ]
    list_display = [
        'name',
        'graduation_year',
        'cr',
        'faculty_advisor'
    ]

admin.site.register(Bracket, BracketAdmin)


class JoinRequestAdmin(admin.ModelAdmin):
    readonly_fields = [
        'account',
        'bracket',
        'date_created',
        'accepted',
    ]
    list_display = [
        'account',
        'bracket',
        'date_created',
        'accepted',
    ]

admin.site.register(JoinRequest, JoinRequestAdmin)
