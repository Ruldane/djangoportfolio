# Generated by Django 2.2.3 on 2019-07-06 18:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20190706_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_pub',
            field=models.DateField(default=datetime.datetime(2019, 7, 6, 18, 44, 24, 545343, tzinfo=utc)),
        ),
    ]