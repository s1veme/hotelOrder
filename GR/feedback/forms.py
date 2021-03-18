from django import forms
from django.db import models
from .models import Reviews
from django.core.exceptions import ValidationError
from snowpenguin.django.recaptcha3.fields import ReCaptchaField



        #Форма отзывов
class ReviewForm(forms.ModelForm):
    captcha = ReCaptchaField()


    class Meta:
        model = Reviews
        fields = ['text', 'name', 'email','captcha']

        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }


    def clean_email(self):
        new_email = self.cleaned_data['email']
        if Reviews.objects.filter(email=new_email).exists():
            raise ValidationError('You cannot reuse the same email')
        return new_email

