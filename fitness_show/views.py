from django.shortcuts import render
from fitness_app.models import Project, Subject, People, Source


def show(request):
    sendtime_dict = Source.objects.order_by('sendtime')[:4]
    # name_dict = People.objects('name')

    context_dict = {'sendtime': sendtime_dict}
    return render(request, "fitness_show/show.html", context_dict)
