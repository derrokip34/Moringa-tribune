from .models import MoringaMerch
from rest_framework import serializers

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoringaMerch
        fields = ('id', 'name', 'description', 'price')