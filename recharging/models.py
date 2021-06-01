from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    mobile = models.BigIntegerField(null=True, blank=True)
    otp = models.IntegerField(default=0)

    def __str__(self):
        return str(self.mobile)


class Plan(models.Model):
    operator = models.CharField(default="", max_length=255)
    type = models.CharField(max_length=255)
    amount = models.IntegerField()
    validity = models.CharField(max_length=255)

    def __str__(self):
        return str(self.operator) + "," + str(self.type)


class Recharge(models.Model):
    recharge_number = models.IntegerField()
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, default=None, blank=True, null=True)

    class Meta:
        verbose_name_plural = "recharge"

    def __str__(self):
        return str(self.recharge_number) + "," + str(self.plan)


class RecentRecharge(models.Model):
    recharged_number = models.ForeignKey(Recharge, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    date = models.DateField()
