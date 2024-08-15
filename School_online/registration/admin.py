from django.contrib import admin
from .models import (
    Student,
    Teacher,
    Parent,
    Enrollment
)

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Enrollment)



