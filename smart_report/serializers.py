from rest_framework import serializers
from rest_framework.fields import JSONField

from smart_report.model import RawData


class InputCreateSerializer(serializers.ModelSerializer):
    session_id = serializers.CharField(source='id', read_only=True)
    body_json = JSONField()

    class Meta:
        model = RawData
        fields = ('session_id', 'platform', 'sender_id', 'receive_id', 'body_json',)
