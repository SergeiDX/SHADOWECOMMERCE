# Generated by Django 5.0.4 on 2024-04-17 02:18

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_payment_orderplaced'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='orderplaced',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]