# Generated by Django 2.0.5 on 2019-07-13 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestBrief', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event_request',
            name='client_remote_work',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
