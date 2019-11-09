from abc import ABC

from rest_framework import serializers


class ProductSerializer(serializers.Serializer, ABC):
    id = serializers.IntegerField(read_only=True)
    owner = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    body = serializers.CharField()
    location = serializers.CharField()
    publication_date = serializers.DateField()
    active = serializers.BooleanField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
