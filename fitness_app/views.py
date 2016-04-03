from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    title_dict = {'tit_head': "vigour"}
    return render(request, 'fitness_app/index.html', title_dict)


def login(request):
    return render(request, 'fitness_app/login.html')
