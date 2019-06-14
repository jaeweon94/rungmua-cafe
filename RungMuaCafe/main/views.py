import csv
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

from django.shortcuts import render
from .models import Feedback
from django.http import HttpResponse


def signin(request):
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Sign in fail, try again.')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return HttpResponse('Sign up complete')
        else:
            return HttpResponse('Sign up fail')
    else:
        form = UserForm()
        return render(request, 'addUser.html', {'form': form})


def home(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {'num_visits': num_visits}
    return render(request, 'home.html', context)


def aboutUs(request):
    return render(request, 'aboutUs.html')


def locations(request):
    csv_path = 'main/static/location.csv'
    csv_file = open(csv_path, 'r')
    csv_obj = csv.DictReader(csv_file)
    csv_list = list(csv_obj)

    return render(request, 'locations.html', {'csv_list': csv_list})


def menu(request):
    return render(request, 'menu.html')


def onlineShopping(request):
    return render(request, 'onlineShopping.html')


def offers(request):
    return render(request, 'offers.html')


def contactUs(request):
    if request.method == 'POST':
        if request.POST.get('Name') and request.POST.get('Email') and request.POST.get('Phone Number') \
                and request.POST.get('Feedback'):
            post = Feedback()
            post.name = request.POST.get('Name')
            post.email = request.POST.get('Email')
            post.phone_number = request.POST.get('Phone Number')
            post.feedback = request.POST.get('Feedback')
            post.save()

            return HttpResponse("Thanks for your feedback!")

    else:
        return render(request, 'contactUs.html')


