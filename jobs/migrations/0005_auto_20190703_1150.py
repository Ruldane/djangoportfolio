# Generated by Django 2.2.3 on 2019-07-03 11:50

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20190701_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='summary',
            field=ckeditor.fields.RichTextField(default='SOME STRING', max_length=800),
        ),
    ]
