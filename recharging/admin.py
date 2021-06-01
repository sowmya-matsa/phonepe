from django.contrib import admin
from .models import Login, Operator, Contacts, Recharge


# Register your models here.
class LoginAdmin(admin.ModelAdmin):
    list_display = ['id', 'mobile_number']


class OperatorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'type_of_recharge', 'amount', 'validity']


class ContactsAdmin(admin.ModelAdmin):
    list_display = ['id', 'contact_name', 'mobile_number', 'user']


class RechargeAdmin(admin.ModelAdmin):
    list_display = ['id', 'contact', 'operand']


admin.site.register(Login, LoginAdmin)
admin.site.register(Operator, OperatorAdmin)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Recharge, RechargeAdmin)
