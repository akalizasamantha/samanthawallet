from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea


class UserAdminConfig(UserAdmin):
    model = Account
    search_fields = ('email', 'user_name', 'first_name','money')
    list_filter = ('email', 'user_name', 'first_name','money', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email', 'user_name','money', 'first_name',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name','money')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('about',)}),
    )
    formfield_overrides = {
        Account.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name','money', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(Account, UserAdminConfig)
