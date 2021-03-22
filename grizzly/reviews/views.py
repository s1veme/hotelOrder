from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.views.generic import ListView
from django.views.generic.base import View

from .models import Review
from .forms import ReviewForm


class ReviewList(ListView):
    model = Review
    queryset = Review.objects.all()
    template_name = 'reviews/reviews.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'reviews': self.queryset})

    def post(self, request, *args, **kwargs):
        bound_form = ReviewForm(request.POST)

        if bound_form.is_valid():
            new_review = bound_form.save()
            return redirect('detail_review_url')
        else:
            return HttpResponse('Неверная форма', status=415)
