# Generated by Django 4.1.3 on 2023-01-16 23:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_rename_ticket_id_userpurchaseditcketslist_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpurchaseditcketslist',
            name='valid_until',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
