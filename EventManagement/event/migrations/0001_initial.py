# Generated by Django 2.0.5 on 2019-07-12 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
        ('agency', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=255, null=True)),
                ('event_venue', models.CharField(max_length=255, null=True)),
                ('event_type', models.CharField(blank=True, max_length=255, null=True)),
                ('event_budget', models.IntegerField(null=True)),
                ('event_guest_number', models.IntegerField(blank=True, null=True)),
                ('event_date', models.DateField(blank=True, null=True)),
                ('event_time', models.TimeField(blank=True, null=True)),
                ('event_remote_arrange', models.CharField(blank=True, max_length=255, null=True)),
                ('event_size', models.CharField(blank=True, max_length=255, null=True)),
                ('event_description', models.CharField(blank=True, max_length=2083, null=True)),
                ('event_username', models.CharField(blank=True, max_length=255, null=True)),
                ('event_agency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='agency.Agency')),
                ('event_client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='client.Client')),
                ('stuff', models.ManyToManyField(to='agency.Staff')),
            ],
        ),
    ]
