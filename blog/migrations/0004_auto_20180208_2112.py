# Generated by Django 2.0.2 on 2018-02-08 15:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180208_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 8, 15, 42, 36, 481671, tzinfo=utc)),
        ),
    ]