# Generated by Django 2.2.2 on 2019-07-01 09:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190630_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_pub',
            field=models.DateField(default=datetime.datetime(2019, 7, 1, 9, 23, 17, 740036, tzinfo=utc)),
        ),
    ]
