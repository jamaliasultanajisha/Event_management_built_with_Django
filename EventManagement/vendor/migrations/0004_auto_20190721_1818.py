# Generated by Django 2.0.5 on 2019-07-21 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0003_vendor_vendor_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='vendor_password',
        ),
        migrations.AlterField(
            model_name='vendor',
            name='vendor_email',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='vendor_name',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
