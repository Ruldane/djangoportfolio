# Generated by Django 2.2.3 on 2019-07-08 06:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20190707_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_pub',
            field=models.DateField(default=datetime.datetime(2019, 7, 8, 6, 49, 12, 726683, tzinfo=utc)),
        ),
    ]
