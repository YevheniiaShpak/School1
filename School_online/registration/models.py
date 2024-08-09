from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model

User = get_user_model()


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    students = models.ManyToManyField('Student', related_name='teachers')

    def __str__(self):
        return self.user.username



class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username


class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    children = models.ManyToManyField('Student', related_name='parents')

    def __str__(self):
        return f'{self.user.username}'


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, null=True, blank=True)
    enroll_date = models.DateField(auto_now=True)

    def __repr__(self):
        return f'Student: {self.student}, Teacher: {self.teacher}, Parent: {self.parent}'

    def __str__(self):
        return f'Student: {self.student}, Teacher: {self.teacher}, Parent: {self.parent}'


