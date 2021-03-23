from django.urls import path

from .views import HomeView, RoomDetail, ReviewList

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('room/<str:slug>', RoomDetail.as_view(), name='room'),
    path('reviews/', ReviewList.as_view(), name='reviews')
]
