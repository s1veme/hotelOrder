from django.urls import path
from django.views.decorators.cache import cache_page

from .views import HomeView, RoomDetail, ReviewList

urlpatterns = [
    path('', cache_page(3600)(HomeView.as_view()), name='home'),
    path('room/<str:slug>', RoomDetail.as_view(), name='room'),
    path('reviews/', ReviewList.as_view(), name='reviews')
]
