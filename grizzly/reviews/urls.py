from django.urls import path

from .views import ReviewList


urlpatterns = [
    path('', ReviewList.as_view()),
]
