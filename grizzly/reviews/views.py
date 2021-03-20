from django.shortcuts import render, redirect

from django.views.generic import ListView
from django.views.generic.base import View

from .models import Review


class ReviewList(ListView):
    model = Review
    queryset = Review.objects.all()
    template_name = 'mainapp/reviews.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'reviews': self.queryset})
