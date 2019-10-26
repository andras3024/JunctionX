# Generated by Django 2.2.5 on 2019-10-26 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tale_app', '0005_auto_20191026_1250'),
        ('children_app', '0001_initial'),
        ('statistics_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='child',
        ),
        migrations.RemoveField(
            model_name='result',
            name='target_emotion',
        ),
        migrations.AddField(
            model_name='result',
            name='content',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='tale_app.Content'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('completed', models.BooleanField(db_column='completed', default=False)),
                ('date', models.DateTimeField(auto_now=True, db_column='date')),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='children_app.Child')),
                ('tale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tale_app.Tale')),
            ],
        ),
        migrations.AddField(
            model_name='result',
            name='session',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='statistics_app.Session'),
            preserve_default=False,
        ),
    ]
