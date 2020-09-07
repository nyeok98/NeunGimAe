from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account

class AccountAdmin(UserAdmin):
    readonly_fields = ('date_joined', 'last_login')
    list_display = ('email', 'username', 'last_login','phone', 'is_admin', 'is_staff')  #admin 에서 보여지는 부분
    search_fields = ('email', 'username')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
