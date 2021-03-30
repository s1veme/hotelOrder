from django import forms
from django.db import models
from .models import Room
from .models import Review, Room

from django.core.exceptions import ValidationError

from snowpenguin.django.recaptcha3.fields import ReCaptchaField
from phonenumber_field.formfields import PhoneNumberField
from django.forms.fields import DateField

from django.contrib.admin.widgets import AdminDateWidget


class ReviewForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Review
        fields = ['text', 'name', 'email', 'captcha']

        widgets = {
            'text': forms.TextInput(attrs={'class': 'form__review', 'type': 'text', 'placeholder': 'Напишите отзыв'}),
            'name': forms.TextInput(attrs={'class': 'review-form__item', 'type': 'text', 'placeholder': 'Имя'}),
            'email': forms.TextInput(attrs={'class': 'review-form__item', 'type': 'text', 'placeholder': 'email'}),
        }

    def clean_email(self):
        new_email = self.cleaned_data['email']
        if Review.objects.filter(email=new_email).exists():
            raise ValidationError('You cannot reuse the same email')
        return new_email


class RoomReservation(forms.Form):

    name = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={'type': 'text', 'placeholder': 'Имя', 'class': 'reservation-form__input'}))
    last_name = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={'type': 'text', 'placeholder': 'Фамилия', 'class': 'reservation-form__input'}))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'type': 'text', 'placeholder': 'email', 'class': 'reservation-form__input'}))
    phone = PhoneNumberField(widget=forms.TextInput(
        attrs={'type': 'text', 'placeholder': 'Номер телефона', 'class': 'reservation-form__input'}))

    title = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, *args, room_slug=None, **kwargs):
        super(forms.Form, self).__init__(*args, **kwargs)
        if room_slug is not None:
            self.fields['title'].initial = Room.objects.get(
                slug=room_slug
            )


class MainRegistrationForm(forms.Form):
    number_selection = forms.ModelChoiceField(
        label="Выбрать номер", empty_label="Номер не выбран", queryset=Room.objects.all(), to_field_name='title', widget=forms.Select(attrs={'class': 'form-select__item'}))

    arrival_date = forms.DateField(
        label="Дата заезда", widget=forms.SelectDateWidget(attrs={'style': 'padding: 10px 3px; text-align: center;'}))

    departure_date = forms.DateField(
        label="Дата отъезда", widget=forms.SelectDateWidget(attrs={'style': 'padding: 10px 3px; text-align: center;'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'style': 'padding: 12px 3px;'}))
