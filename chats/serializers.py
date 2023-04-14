from rest_framework import serializers
from accounts.models import CustomUser
from .models import Thread, Message


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ("id", "username", "email", "password")


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ("id", "sender", "text", "thread", "created", "is_read")


class ThreadSerializer(serializers.ModelSerializer):
    participants = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), many=True)

    def validate_participants(self, value):
        if len(value) > 2:
            raise serializers.ValidationError('Thread can have a maximum of 2 participants')
        return value

    class Meta:
        model = Thread
        fields = ("id", "participants", "created", "updated")




