from rest_framework import viewsets
from django.shortcuts import render, redirect
from rest_framework.permissions import IsAuthenticated
from .models import Chat, Message, Comment
from .serializers import ChatSerializer, MessageSerializer, CommentSerializer
from django.contrib.auth.decorators import login_required
from registration.models import Teacher
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied


@login_required
def create_comment(request):
    if request.method == 'POST':
        message_id = request.POST.get('message_id')
        content = request.POST.get('comment')

        try:
            message = Message.objects.get(id=message_id)
        except Message.DoesNotExist:
            return redirect('chat_page')

        if request.user.groups.filter(name='Teachers').exists():
            Comment.objects.create(
                message=message,
                commenter=request.user,
                content=content
            )

        return redirect('chat_page')


@login_required
def chat_page(request):
    messages = Message.objects.all().select_related('sender', 'recipient')
    teachers = Teacher.objects.all()

    if request.method == 'POST':
        if 'message' in request.POST:
            recipient_id = request.POST.get('recipient')
            message_text = request.POST.get('message')
            recipient = Teacher.objects.get(id=recipient_id)

            #chat, created = Chat.objects.get_or_create(participants__in=[request.user, recipient.user])
            Message.objects.create(
                chat=Chat.objects.first(),
                sender=request.user,
                recipient=recipient.user,
                content=message_text
            )
        elif 'comment' in request.POST:
            message_id = request.POST.get('message_id')
            comment_text = request.POST.get('comment')
            message = Message.objects.get(id=message_id)

            if request.user in message.chat.participants.all() and isinstance(request.user, Teacher):
                Comment.objects.create(
                    message=message,
                    commenter=request.user,
                    content=comment_text
                )

    return render(request, 'chat/chat_page.html', {
        'messages': messages,
        'teachers': teachers,
    })


class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def send_message(self, request, pk=None):
        chat = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(sender=request.user, chat=chat)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.groups.filter(name='Teachers').exists():
            serializer.save(sender=self.request.user)
        else:
            raise PermissionDenied("Ви не маєте дозволу коментувати.")
