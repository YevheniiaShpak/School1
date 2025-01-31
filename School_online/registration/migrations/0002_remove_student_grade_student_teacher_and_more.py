# Generated by Django 5.1 on 2024-08-09 15:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='grade',
        ),
        migrations.AddField(
            model_name='student',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.teacher'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='students',
            field=models.ManyToManyField(related_name='teachers', to='registration.student'),
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enroll_date', models.DateField(auto_now=True)),
                ('students', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('children', models.ManyToManyField(related_name='parents', to='registration.student')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
