from django.contrib.postgres.fields import JSONField
from django.db import models


class RawData(models.Model):
    platform = models.CharField(max_length=20)
    sender_id = models.CharField(max_length=100)
    receive_id = models.CharField(max_length=100)
    body_json = JSONField()
    ack_date = models.DateTimeField(auto_now_add=True)


class RealData(models.Model):
    session = models.ForeignKey(RawData, on_delete=models.PROTECT)
    body_clean_json = JSONField()
    ack_date = models.DateTimeField(auto_now_add=True)


class Information(models.Model):
    session = models.ForeignKey(RawData, on_delete=models.PROTECT)
    information_json = JSONField()
