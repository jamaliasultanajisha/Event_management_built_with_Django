# Generated by Django 2.0.5 on 2019-07-22 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0008_auto_20190721_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendorbrief',
            name='vendor_service',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
