# Generated by Django 2.0.2 on 2018-02-08 15:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180208_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 8, 15, 52, 7, 347928, tzinfo=utc)),
        ),
    ]