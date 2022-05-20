from django.db import models


class Pereval_added(models.Model):
    beautyTitle = models.CharField(max_length=64, null=True)
    title = models.CharField(max_length=64, default='title')  # TODO delete default
    other_titles = models.CharField(max_length=64, null=True)
    connect = models.CharField(max_length=64, null=True)
    add_time = models.CharField(max_length=64, default='add_time')  # TODO delete default
    user = models.JSONField(null=True)  # TODO null
    coords = models.JSONField(null=True)  # TODO null
    type = models.CharField(max_length=64, default='pass')
    level = models.JSONField(null=True)  # TODO null
    status = models.CharField(max_length=16, default='new')

    class Meta:
        db_table = 'pereval_added'


class Pereval_images(models.Model):
    date_added = models.CharField(max_length=128, null=True)
    img = models.ImageField()
    blob = models.BinaryField()
    id_pereval = models.IntegerField(default=3)  # TODO delete default
    comment = models.TextField(null=True)
    title = models.CharField(max_length=128, null=True)

    class Meta:
        db_table = 'pereval_images'
