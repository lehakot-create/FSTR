from django.db import models


class Pereval_added(models.Model):
    beautyTitle = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    other_titles = models.CharField(max_length=64)
    connect = models.CharField(max_length=64, blank=True)
    add_time = models.CharField(max_length=64)
    user = models.JSONField()
    coords = models.JSONField()
    type = models.CharField(max_length=64, default='pass')
    level = models.JSONField()
    images = models.JSONField()
    status = models.CharField(max_length=16, default='new')

    class Meta:
        db_table = 'pereval_added'


class Pereval_images(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    blob = models.BinaryField(null=False)

    class Meta:
        db_table = 'pereval_images'
