from django.db import models


class Tale(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    name = models.CharField(db_column='name', max_length=128, blank=True, null=True)
    image = models.ImageField(db_column='image', upload_to='tale_app/pictures', blank=True)

    class Meta:
        db_table = 'tale'

    def __str__(self):
        return 'ID:{} Name:{}'.format(self.id, self.name)


class Content(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    taleid = models.ForeignKey(Tale, models.CASCADE, db_column='taleid')
    mp4 = models.CharField(db_column='mp4', max_length=256, blank=True, null=True)
    taskid = models.IntegerField(db_column='taskid', null=True, blank=True)
    targetemotion = models.IntegerField(db_column='targetemotion')
    order = models.IntegerField(db_column='order', null=False)

    class Meta:
        db_table = 'content'

    def __str__(self):
        return 'ID:{} Name:{}'.format(self.id, self.name)