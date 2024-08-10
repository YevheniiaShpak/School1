from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from .models import UserActivity
from registration.models import Student

@receiver(post_save, sender=User)
def create_user_activity(sender, instance, created, **kwargs):
    if created:
        UserActivity.objects.create(user=instance)

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    if Student.objects.filter(user=user).exists():
        UserActivity.objects.update_or_create(user=user, defaults={'is_online': True})

@receiver(user_logged_out)
def update_user_offline(sender, request, user, **kwargs):
    activity, created = UserActivity.objects.get_or_create(user=user)
    activity.is_online = False
    activity.save()


@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    if Student.objects.filter(user=user).exists():
        UserActivity.objects.update_or_create(user=user, defaults={'is_online': False})
