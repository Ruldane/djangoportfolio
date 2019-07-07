# Generated by Django 2.2.3 on 2019-07-06 18:28

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20190703_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_skills', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images/')),
                ('body', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='formations',
            name='body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='summary',
            field=ckeditor.fields.RichTextField(default='SOME STRING'),
        ),
    ]