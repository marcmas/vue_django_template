from unicodedata import name
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('index/', TemplateView.as_view(template_name='polls2/index.html'), name="index"),
]