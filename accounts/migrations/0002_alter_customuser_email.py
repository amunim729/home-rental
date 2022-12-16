# Generated by Django 4.1.4 on 2022-12-15 10:11

import accounts.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=accounts.models.LowercaseEmailField(max_length=254, unique=True),
        ),
    ]
