# Generated by Django 2.0.5 on 2019-07-20 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0004_auto_20190720_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminagency_transaction',
            name='agency_country',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]