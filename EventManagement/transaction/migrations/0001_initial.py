# Generated by Django 2.0.5 on 2019-07-12 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
        ('agency', '0001_initial'),
        ('vendor', '0001_initial'),
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminAgency_Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_agency_pay_method', models.CharField(max_length=255)),
                ('admin_agency_pay_status', models.CharField(max_length=255)),
                ('agency', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='agency.Agency')),
            ],
        ),
        migrations.CreateModel(
            name='ClientAgency_Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_agency_pay_method', models.CharField(max_length=255)),
                ('client_agency_pay_status', models.CharField(max_length=255)),
                ('agency', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='agency.Agency')),
                ('client', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='client.Client')),
                ('event', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='event.Event')),
            ],
        ),
        migrations.CreateModel(
            name='ClientService_Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_service_pay_method', models.CharField(max_length=255)),
                ('client_service_pay_status', models.CharField(max_length=255)),
                ('client', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='client.Client')),
                ('event', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='event.Event')),
                ('vendor', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='vendor.Vendor')),
            ],
        ),
    ]