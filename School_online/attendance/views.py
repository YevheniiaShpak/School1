from django.shortcuts import render
from .models import UserActivity

def attendance_view(request):
    activities = UserActivity.objects.all()
    return render(request, 'attendance/attendance.html', {'activities': activities})

