# Generated by Django 2.0.5 on 2019-07-13 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0004_auto_20190712_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agencybrief',
            name='agency_budget_lower',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='agencybrief',
            name='agency_budget_upper',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
