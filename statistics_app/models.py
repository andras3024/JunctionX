from django.db import models
from children_app.models import Child
# from tale_app import Tale, Content


class Result(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    child = models.ForeignKey(Child, models.CASCADE)
    # tale = models.ForeignKey(Tale, models.CASCADE)
    # content = models.ForeignKey(Content, models.CASCADE)
    target_emotion = models.IntegerField()
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
        return 'ID: {} Child name: {}'.format(self.id, self.child.name)
