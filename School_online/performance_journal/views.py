from django.shortcuts import render, redirect
from .models import Grade
from registration.models import Teacher
from .forms import GradeForm
from django.contrib.auth.decorators import login_required, user_passes_test


def is_teacher(user):
    return user.groups.filter(name='Teachers').exists()


@login_required
#@user_passes_test(is_teacher)
def add_grade_view(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            grade = form.save(commit=False)
            teacher = Teacher.objects.get(user=request.user)
            grade.teacher = teacher
            grade.save()
            return redirect('performance_journal:grades_list')
    else:
        form = GradeForm()
    return render(request, 'performance_journal/add_grade.html', {'form': form})


@login_required
def grades_list_view(request):
    grades = Grade.objects.all()
    return render(request, 'performance_journal/grades_list.html', {'grades': grades})

