from django.urls import path
from django.views.generic import TemplateView

app_name = "stockpredictor"
urlpatterns = [
    path("", TemplateView.as_view(template_name="stockpredictor/index.html")),
]
