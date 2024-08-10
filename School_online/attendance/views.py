from django.shortcuts import render
from .models import UserActivity
from django.contrib.auth.decorators import login_required


@login_required
def attendance_view(request):
    activities = UserActivity.objects.all()
    return render(request, 'attendance/attendance.html', {'activities': activities})

