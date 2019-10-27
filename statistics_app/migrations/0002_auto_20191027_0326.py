# Generated by Django 2.1.13 on 2019-10-27 02:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tale_app', '0001_initial'),
        ('children_app', '0003_child_emojitype'),
        ('statistics_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('completed', models.BooleanField(db_column='completed', default=False)),
                ('date', models.DateTimeField(auto_now=True, db_column='date')),
                ('content_id', models.IntegerField()),
                ('image_path', models.CharField(blank=True, db_column='image_path', max_length=255)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='children_app.Child')),
                ('tale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tale_app.Tale')),
            ],
        ),
        migrations.AddField(
            model_name='result',
            name='content',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tale_app.Content'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='result',
            name='image',
            field=models.ImageField(blank=True, db_column='image', upload_to='azure_app/pictures'),
        ),
        migrations.AlterField(
            model_name='result',
            name='emotion_0',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='emotion_1',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='emotion_2',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='emotion_3',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='emotion_4',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='emotion_5',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='emotion_6',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='emotion_7',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='result',
            name='session',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='statistics_app.Session'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='result',
            name='child',
        ),
        migrations.RemoveField(
            model_name='result',
            name='target_emotion',
        ),
        migrations.AlterUniqueTogether(
            name='result',
            unique_together={('session', 'content')},
        ),
    ]
