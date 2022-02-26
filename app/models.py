from django.db import models


class Pereval_added(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    raw_data = models.JSONField()
    images = models.JSONField()
    status = models.CharField(max_length=16)

    class Meta:
        db_table = 'pereval_added'


class Pereval_images(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    img = models.BinaryField(null=False)

    class Meta:
        db_table = 'pereval_images'
