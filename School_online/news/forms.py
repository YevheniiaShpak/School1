from django.forms import ModelForm
from .models import Articles
from django.utils import timezone

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

    def save(self, commit=True):
        article = super().save(commit=False)
        if not article.date:
            article.date = timezone.now()
        if commit:
            article.save()
        return article

