from django.db import models
from django.contrib.auth import get_user_model
from registration.models import Student, Teacher

User = get_user_model()


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    grade = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.student} - {self.subject} - {self.grade}'
