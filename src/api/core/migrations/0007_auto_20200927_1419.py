# Generated by Django 3.0.8 on 2020-09-27 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200927_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='address',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
