# Generated by Django 3.2.3 on 2021-06-01 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recharging', '0003_plan_operator'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recharge',
            old_name='mobile_number',
            new_name='recharge_number',
        ),
    ]
