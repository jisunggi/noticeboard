# Generated by Django 5.0.1 on 2024-02-01 06:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0002_notice_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='password',
            field=models.CharField(max_length=4, validators=[django.core.validators.MinLengthValidator(limit_value=4)]),
        ),
    ]