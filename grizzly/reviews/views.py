from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView
from django.views.generic.base import View
from .models import *
from .forms import ReviewForm
from django.conf import settings
from g_recaptcha.validate_recaptcha import validate_captcha


# Форма отзывов
class Add_Review(View):
    def get(self, request):
        form = ReviewForm()
        context["form"] = ReviewForm()
        return render(request, 'reviews.html', context={'form': form})

    # Проверка на валидность
    def post(self, request):
        bound_form = ReviewForm(request.POST)

        if bound_form.is_valid():
            new_review = bound_form.save()
            return redirect('detail_review_url')
        return render(request, 'reviews.html', context={'form': bound_form})


def review_detail(request):
    review = Review.objects.all()
    return render(request, 'see_reviews.html', context={'review': review})
