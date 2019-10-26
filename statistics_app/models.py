from django.db import models
from children_app.models import Child
from tale_app.models import Tale, Content


class Session(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    tale = models.ForeignKey(Tale, models.CASCADE)
    child = models.ForeignKey(Child, models.CASCADE)
    completed = models.BooleanField(db_column='completed', default=False)
    date = models.DateTimeField(db_column='date', auto_now=True)
    content_id = models.IntegerField()
    image = models.ImageField(db_column='image', upload_to='statistics_app/pictures', blank=True)

    def __str__(self):
        return 'ID: {} Child name: {} Tale: {}'.format(self.id, self.child.name, self.tale.name)


class Result(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    session = models.ForeignKey(Session, models.CASCADE)
    content = models.ForeignKey(Content, models.CASCADE)
    emotion_0 = models.FloatField()
    emotion_1 = models.FloatField()
    emotion_2 = models.FloatField()
    emotion_3 = models.FloatField()
    emotion_4 = models.FloatField()
    emotion_5 = models.FloatField()
    emotion_6 = models.FloatField()
    emotion_7 = models.FloatField()
    time = models.DateTimeField(db_column='time', auto_now=True)

    class Meta:
        db_table = 'result'

    def __str__(self):
        return 'ID: {} Child name: {}'.format(self.id, self.session.child.name)
