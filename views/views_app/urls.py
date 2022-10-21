from django.urls import path
from .views import NewsList, NewsItem


urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', NewsItem.as_view())
]
