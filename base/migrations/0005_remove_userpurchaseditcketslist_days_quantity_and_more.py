# Generated by Django 4.1.3 on 2023-01-16 23:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_userpurchaseditcketslist_days_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpurchaseditcketslist',
            name='days_quantity',
        ),
        migrations.RemoveField(
            model_name='userpurchaseditcketslist',
            name='type',
        ),
        migrations.AddField(
            model_name='userpurchaseditcketslist',
            name='ticket_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.ticketslist'),
        ),
        migrations.AddField(
            model_name='userpurchaseditcketslist',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userpurchaseditcketslist',
            name='valid_until',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='user',
            name='funds',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userpurchaseditcketslist',
            name='lines',
            field=models.CharField(default='', max_length=255),
        ),
    ]
