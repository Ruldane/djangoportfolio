# Generated by Django 2.2.2 on 2019-07-01 09:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190701_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_pub',
            field=models.DateField(default=datetime.datetime(2019, 7, 1, 9, 29, 15, 42751, tzinfo=utc)),
        ),
    ]
