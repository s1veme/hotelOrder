from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.contrib import messages

from django.views.generic.base import View
from django.views.generic import DetailView, ListView

from .models import Gallery, Room, Image, Review
from .forms import ReviewForm, RoomReservation, MainRegistrationForm

from .utils import sendMessage as sm

email = sm.sendMessageToGmail()


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
        return render (request,'mainapp/home.html', context=self.create_context(bound_form))

    def create_context(self, bound_form):
        gallery = Gallery.objects.all()
        rooms = Room.objects.all()
        form_review = ReviewForm()
        form_reservation = MainRegistrationForm()
        queryset_dict = {'images': gallery, 'rooms': rooms,
                     'form': bound_form, 'form_reservation': form_reservation}
        
        return queryset_dict
        

class HomeView(View):
    gallery = Gallery.objects.all()
    rooms = Room.objects.all()
    form_review = ReviewForm()
    form_reservation = MainRegistrationForm()

    queryset_dict = {'images': gallery, 'rooms': rooms,
                     'form': form_review, 'form_reservation': form_reservation}

    def get(self, request, *args, **kwargs):
        return render(request, 'mainapp/home.html', self.queryset_dict)

    def post(self, request, *args, **kwargs):
        data = request.POST
        bound_form = MainRegistrationForm(data)

        if bound_form.is_valid():
            text = sm.generate_message_registration(data.dict())

            # email.create_message(text)
            # email.send_message()

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
        data = request.POST
        data = data.copy()

        if not data['phone'].startswith('+'):
            data['phone'] = f'+{data["phone"]}'

        bound_form = RoomReservation(data)

        if bound_form.is_valid():
            text = sm.generate_message(data.dict())
            messages.success(request, 'Ваша заявка успешно отправлена!')
            # email.create_message(text)
            # email.send_message()

        return redirect('home')
