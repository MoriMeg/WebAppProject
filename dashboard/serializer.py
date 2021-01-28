from rest_framework import serializers
from .models import ConsumableModel


class ConsumableSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsumableModel
        fields = ('datetime', 'elapsed_time', 'elapsed_days')
