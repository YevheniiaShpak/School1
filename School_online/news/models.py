from django.db import models
from django.utils import timezone

class Articles(models.Model):
    title = models.CharField('Назва', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статті')
    date = models.DateTimeField('Дата публікації', default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новини'
        verbose_name_plural = 'Новини'
