# Generated by Django 3.0.8 on 2020-09-27 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200926_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_time',
            field=models.DateTimeField(null=True),
        ),
    ]