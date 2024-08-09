from django.urls import path
from .views import attendance_view

urlpatterns = [
    path('attendance/', attendance_view, name='attendance'),
]
