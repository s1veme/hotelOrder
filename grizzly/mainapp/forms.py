from django import forms
from django.db import models
from django.core.exceptions import ValidationError
from snowpenguin.django.recaptcha3.fields import ReCaptchaField

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
