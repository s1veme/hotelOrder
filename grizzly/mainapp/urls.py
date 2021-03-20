from django.urls import path

from .views import HomeView, RoomDetail

urlpatterns = [
    path('', HomeView.as_view()),
    path('room/<str:slug>', RoomDetail.as_view(), name='room')
]
