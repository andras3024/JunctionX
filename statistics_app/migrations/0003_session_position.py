# Generated by Django 2.2.5 on 2019-10-26 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistics_app', '0002_auto_20191026_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='position',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
