from django.test import TestCase
from .models import Articles

class ArticlesModelTest(TestCase):

    def setUp(self):
        self.article = Articles.objects.create(
            title="Тестовая статья",
            anons="Краткий анонс",
            full_text="Полный текст",
            date="2024-08-15"
        )

    def test_article_creation(self):
        self.assertIsInstance(self.article, Articles)
        self.assertEqual(self.article.title, "Тестовая статья")


