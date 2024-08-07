from django.urls import path
from .views import register_view, login_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('', login_view, name='home'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)