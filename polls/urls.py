from unicodedata import name
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='polls/index.html'), name="index"),
]