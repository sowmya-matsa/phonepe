from django.db import models


# Create your models here.
class Login(models.Model):
    mobile_number = models.BigIntegerField()
    otp = models.IntegerField()

    def __str__(self):
        return str(self.mobile_number)

    class Meta:
        verbose_name_plural = "login"


class Operator(models.Model):
    name = models.CharField(max_length=255)
    type_of_recharge = models.CharField(max_length=255)
    amount = models.IntegerField()
    validity = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class Contacts(models.Model):
    contact_name = models.CharField(max_length=255)
    mobile_number = models.IntegerField()
    user = models.ForeignKey(Login, on_delete=models.SET_NULL, default=None, blank=True, null=True)

    def __str__(self):
        return str(self.contact_name)

    class Meta:
        verbose_name_plural = "contacts"


class Recharge(models.Model):
    contact = models.ForeignKey(Contacts, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    operand = models.ForeignKey(Operator, on_delete=models.SET_NULL, default=None, blank=True, null=True)

    class Meta:
        verbose_name_plural = "recharge"
