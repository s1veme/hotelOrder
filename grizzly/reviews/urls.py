from django.urls import path
from .import views
from .models import *
from .views import Add_Review, review_detail


urlpatterns = [
    path("", Add_Review.as_view(), name='add_review_url'),
    path("see_reviews/", review_detail, name="detail_review_url")
]