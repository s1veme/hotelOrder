from django.shortcuts import render

from django.views.generic.base import View
from django.views.generic import DetailView

from .models import Gallery, Room, Image


class HomeView(View):
    gallery = Gallery.objects.all()
    rooms = Room.objects.all()

    queryset_dict = {'images': gallery, 'rooms': rooms}

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

        context.update({'images': images})

        return context
