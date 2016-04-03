from django.shortcuts import render
from django.http import HttpResponse
from fitness_app.models import Subject,Project
# Create your views here.


def index(request):
    title_dict = {'tit_head': "vigour"}
    return render(request, 'fitness_app/index.html', title_dict)


def login(request):
    return render(request, 'fitness_app/login.html')
    
def sub(request):
    sub_item = Project.objects.all()
    context_dict={}
    context_dict['project']=sub_item
    return render(request,'fitness_app/sub.html',context_dict)
