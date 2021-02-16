from django.contrib import admin
from accounts.models import Account
from django.contrib.auth.admin import UserAdmin
from brackets.models import Bracket


class AccountAdmin(UserAdmin):
    list_display = (
        'username',
        'role',
        'email',
        'date_joined',
        'last_login',
        'is_admin',
    )
    search_fields = (
        'username',
        'role',
        'email',
        'date_joined',
        'last_login',
        'is_admin',
    )
    readonly_fields = (
        'date_joined',
        'last_login',
    )
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)



