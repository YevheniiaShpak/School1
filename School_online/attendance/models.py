from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class UserActivity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_login = models.DateTimeField(auto_now=True)
    is_online = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {"Online" if self.is_online else "Offline"}'




