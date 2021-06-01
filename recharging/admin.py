from django.contrib import admin
from .models import CustomUser, Plan, Recharge,RecentRecharge
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class PlanAdmin(admin.ModelAdmin):
    list_display = ['id', "operator", 'type', 'amount', 'validity']


class RechargeAdmin(admin.ModelAdmin):
    list_display = ['id', 'recharge_number', 'plan', 'user']

class RecentRechargeAdmin(admin.ModelAdmin):
    list_display = ['id','recharged_number','date']

admin.site.register(CustomUser)
admin.site.register(Plan, PlanAdmin)
admin.site.register(Recharge, RechargeAdmin)
admin.site.register(RecentRecharge,RecentRechargeAdmin)
