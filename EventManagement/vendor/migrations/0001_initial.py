# Generated by Django 2.0.5 on 2019-07-12 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(max_length=255)),
                ('vendor_email', models.CharField(max_length=255)),
                ('vendor_password', models.CharField(max_length=255)),
                ('vendor_company_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('vendor_company_website', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('vendor_establish_time', models.IntegerField(blank=True, default=None, null=True)),
                ('vendor_employee_number', models.IntegerField(blank=True, default=None, null=True)),
                ('vendor_annual_turnover', models.IntegerField(blank=True, default=None, null=True)),
                ('vendor_member_type', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('vendor_remote_work', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('vendor_description', models.CharField(blank=True, default=None, max_length=2083, null=True)),
                ('vendor_logo', models.CharField(blank=True, default=None, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_company_address', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('vendor_contact_number', models.IntegerField(blank=True, default=None, null=True)),
                ('vendor_social_media', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('vendor_specialty', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('vendor_past_work', models.CharField(blank=True, default=None, max_length=2083, null=True)),
                ('vendor_upcoming_work', models.CharField(blank=True, default=None, max_length=2083, null=True)),
                ('vendor_provide_design', models.CharField(blank=True, default=None, max_length=2083, null=True)),
                ('vendor_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor.Vendor')),
            ],
        ),
        migrations.AddField(
            model_name='service_type',
            name='vendor_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor.Vendor'),
        ),
    ]
