from django.urls import path
from .views import news_home, create

urlpatterns = [
    path('', news_home, name='news_home'),
    path('create', create, name='create'),
]
