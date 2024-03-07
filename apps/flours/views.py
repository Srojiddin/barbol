from django.shortcuts import render
from django.views import generic
from apps.flours.models import Flour


class FlourListView(generic.ListView):
    model = Flour
    template_name = 'index.html'


def about(request):
    return render(request, 'about.html')
