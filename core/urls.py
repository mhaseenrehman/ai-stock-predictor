from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("stockpredictor.urls", namespace="stockpredictor")),
    path("api/", include("stockpredictor_api.urls", namespace="stockpredictor_api"))
]
