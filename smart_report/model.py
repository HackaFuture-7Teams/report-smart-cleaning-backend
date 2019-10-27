from django.contrib.postgres.fields import JSONField
from django.db import models


class RawData(models.Model):
    platform = models.CharField(max_length=20)
    sender_id = models.CharField(max_length=20)
    receive_id = models.CharField(max_length=20)
    body_json = JSONField()
    ack_date = models.DateTimeField(auto_now_add=True)
