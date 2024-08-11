from django.urls import path
from .views import add_grade_view, grades_list_view

app_name = 'performance_journal'

urlpatterns = [
    path('add/', add_grade_view, name='add_grade'),
    path('', grades_list_view, name='grades_list'),
]
