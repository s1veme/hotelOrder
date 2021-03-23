from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.views.generic.base import View
from django.views.generic import DetailView, ListView

from .models import Gallery, Room, Image, Review
from .forms import ReviewForm, RoomReservation


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
            return redirect('reviews')
        return render(request, self.template_name, {'reviews': self.queryset})


class HomeView(View):
    gallery = Gallery.objects.all()
    rooms = Room.objects.all()
    form = ReviewForm()

    queryset_dict = {'images': gallery, 'rooms': rooms, 'form': form}

    def get(self, request, *args, **kwargs):
        return render(request, 'mainapp/home.html', self.queryset_dict)


class RoomDetail(DetailView):
    model = Room
    queryset = Room.objects.all()

    template_name = 'mainapp/room.html'
    slug_field = "slug"

    def get_context_data(self, **kwargs):
        context = super(RoomDetail, self).get_context_data(**kwargs)

        slug = self.kwargs['slug']
        images = Image.objects.filter(room__slug=slug)
        form = RoomReservation(room_slug=slug)

        context.update({'images': images, 'form': form})

        return context

    def post(self, request, *args, **kwargs):

        # if bound_form.is_valid():
        #    return redirect('home')

        print(request.POST)

        return redirect('home')
