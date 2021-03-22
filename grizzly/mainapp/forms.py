
from django import forms
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.core.exceptions import ValidationError
from snowpenguin.django.recaptcha3.fields import ReCaptchaField
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from .models import Room


from .models import Review


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


class Room_Reservation(forms.Form):
    name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField()
    phone = PhoneNumberField(null=False, blank=False, unique=True)

    widgets = {
                'last_name': forms.TextInput(attrs={'class': 'Room_Reservation', 'type': 'text', 'placeholder': 'Фамилия'}),
                'name': forms.TextInput(attrs={'class': 'Room_Reservation', 'type': 'text', 'placeholder': 'Имя'}),               
                'email': forms.TextInput(attrs={'class': 'Room_Reservation', 'type': 'text', 'placeholder': 'email'}),
                'phone': forms.TextInput(attrs={'class': 'Room_Reservation', 'type': 'text', 'placeholder': 'Номер Телефона'}),
}

    def clean_email(self):
        new_email = self.cleaned_data['email']
        if Review.objects.filter(email=new_email).exists():
            raise ValidationError('You cannot reuse the same email')
        return new_email


class Main_Registration_Form(forms.Form):
    number_selection = forms.ModelChoiceField(label="Выбрать номер", empty_label="Категория не выбрана", queryset=Room.objects.all())
    arrival_date = forms.DateField(label="Дата заезда", widget=AdminDateWidget)
    departure_date = forms.DateField(label="Дата отъезда",widget=AdminDateWidget)
    email = forms.EmailField()

    widgets = {
                'number_selection': forms.TextInput(attrs={'class': 'Main_Registration_Form', 'type': 'text'}),
                'arrival date': forms.TextInput(attrs={'class': 'Main_Registration_Form', 'type': 'text'}),               
                'departure date': forms.TextInput(attrs={'class': 'Main_Registration_Form', 'type': 'text'}),
                'email': forms.TextInput(attrs={'class': 'Main_Registration_Form', 'type': 'text', 'placeholder': 'email'}),
}

