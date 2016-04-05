from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from fitness_app.models import Subject, Project, People
from fitness_app.forms import Peopleforms
# Create your views here.


def index(request):
    title_dict = {'tit_head': "vigour"}
    return render(request, 'fitness_app/index.html', title_dict)


def sub(request):
    sub_item = Project.objects.all()
    context_dict = {}
    context_dict['project'] = sub_item
    return render(request, 'fitness_app/sub.html', context_dict)


def userlogin(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=name, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/fitness_app/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(name, password)
            return HttpResponse("Invalid login details suplied")
    else:
        return render(request, 'fitness_app/login.html', {})


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = Peopleforms(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print user_form.errors
    else:
        user_form = Peopleforms()
    return render(request, 'fitness_app/register.html',
                  {'user_form': user_form,
                   'registered': registered})
