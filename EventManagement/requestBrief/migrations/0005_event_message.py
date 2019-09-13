# Generated by Django 2.0.5 on 2019-07-15 07:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestBrief', '0004_event_request_client_remote_work'),
    ]

    operations = [
        migrations.CreateModel(
            name='event_message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('client_email', models.EmailField(blank=True, default=None, max_length=255, null=True)),
                ('agency_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('agency_email', models.EmailField(blank=True, default=None, max_length=255, null=True)),
                ('email_subject', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('email_content', models.CharField(blank=True, default=None, max_length=2083, null=True)),
                ('date_added', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]