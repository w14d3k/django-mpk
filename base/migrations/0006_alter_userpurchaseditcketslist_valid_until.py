# Generated by Django 4.1.3 on 2023-01-16 23:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_userpurchaseditcketslist_days_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpurchaseditcketslist',
            name='valid_until',
            field=models.DateField(default=datetime.date),
        ),
    ]