# Generated by Django 3.2.3 on 2021-06-01 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recharging', '0002_auto_20210601_1238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operator',
            name='data',
        ),
        migrations.RemoveField(
            model_name='operator',
            name='talk_time',
        ),
    ]
