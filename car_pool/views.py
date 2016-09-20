from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Car
from .forms import CarForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def post_cars(request):
    cars = Car.objects.all()
    return render(request, 'car_pool/post_cars.html', {'cars': cars})

def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'car_pool/car_detail.html', {'car': car})

def car_booked(request, pk):
    car = get_object_or_404(Car, pk=pk)
    car.book_seat()
    return render(request, 'car_pool/car_booked.html', {'car': car})

@login_required
def new_car(request):
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.driver = request.user
            car.save()
            return redirect('car_detail', pk=car.pk)
    else:
        form = CarForm()
    return render(request, 'car_pool/car_edit.html', {'form': form})

def new_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            authenticate(username=new_user.username, password=new_user.password)
            #redirect, or however you want to get to the main view
            return redirect('post_cars')
    else:
        form = UserForm()
    return render(request, 'car_pool/adduser.html', {'form': form})

@login_required
def car_edit(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == "POST":
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            car = form.save(commit=False)
            car.driver = request.user
            car.save()
            return redirect('car_detail', pk=car.pk)
    else:
        form = CarForm(instance=car)
    return render(request, 'car_pool/car_edit.html', {'form': form})
