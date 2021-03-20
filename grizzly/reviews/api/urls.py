from django.urls import path

from rest_framework import routers

from .views import ReviewView

router = routers.SimpleRouter()

urlpatterns = [
    path('create-review/', ReviewView.as_view())
]

urlpatterns += router.urls
