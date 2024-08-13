from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChatViewSet, MessageViewSet, chat_page, create_comment

router = DefaultRouter()
router.register(r'chats', ChatViewSet, basename='chat')
router.register(r'messages', MessageViewSet, basename='message')

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include(router.urls)),
    path('chat/', chat_page, name='chat_page'),
    path('comment/', create_comment, name='comment_create'),
]
