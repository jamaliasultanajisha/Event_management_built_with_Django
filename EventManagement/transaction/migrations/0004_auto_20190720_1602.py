# Generated by Django 2.0.5 on 2019-07-20 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0003_auto_20190720_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminagency_transaction',
            name='agency_card_month',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='adminagency_transaction',
            name='agency_card_year',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]