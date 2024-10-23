from django.urls import path
from .views import StockAPIView

app_name = "stockpredictor_api"
urlpatterns = [
    path("", StockAPIView.as_view(), name="listcreate"),
    #path("<int:pk>/", StockDetail.as_view(), name="detailcreate")
]
