# Generated by Django 3.2.3 on 2021-06-01 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recharging', '0002_alter_customuser_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='operator',
            field=models.CharField(default='', max_length=255),
        ),
    ]