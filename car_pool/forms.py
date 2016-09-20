from django import forms
from .models import Car
from django.contrib.auth.models import User

class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = ('title','origin', 'destination',
                  'available_seats', 'departing_date', 'arrival_date')


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
