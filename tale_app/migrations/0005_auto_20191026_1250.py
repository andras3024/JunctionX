# Generated by Django 2.2.5 on 2019-10-26 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tale_app', '0004_auto_20191026_0633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='taskid',
        ),
        migrations.AddField(
            model_name='tale',
            name='level',
            field=models.IntegerField(db_column='level', default=1),
            preserve_default=False,
        ),
    ]