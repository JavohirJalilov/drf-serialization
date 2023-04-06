from rest_framework import serializers


class TaskSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=64)
    description = serializers.TextField()
    completed   = serializers.BooleanField(default=False, blank=True)
