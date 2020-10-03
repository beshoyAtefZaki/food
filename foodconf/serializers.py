from rest_framework import serializers


from .models import Unit




class AccountSerializer(serializers.Serializer):
    # idd = serializers.IntegerField(read_only=True)
    description = serializers.CharField(required=False, allow_blank=True, max_length=200)
    home_standrd  = serializers.CharField(required=False, allow_blank=True, max_length=200)
    item_group = serializers.CharField(required=False, allow_blank=True, max_length=200)