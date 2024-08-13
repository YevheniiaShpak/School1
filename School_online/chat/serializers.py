from rest_framework import serializers
from .models import Chat, Message, Comment
from django.contrib.auth import get_user_model

User = get_user_model()


class ChatSerializer(serializers.ModelSerializer):
    participants = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Chat
        fields = ['id', 'participants']


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    recipient = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    chat = serializers.PrimaryKeyRelatedField(queryset=Chat.objects.all())

    class Meta:
        model = Message
        fields = ['id', 'chat', 'sender', 'recipient', 'content', 'timestamp']


class CommentSerializer(serializers.ModelSerializer):
    commenter = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    message = serializers.PrimaryKeyRelatedField(queryset=Message.objects.all())

    class Meta:
        model = Comment
        fields = ['id', 'message', 'commenter', 'content', 'timestamp']
