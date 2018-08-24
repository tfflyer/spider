from django.shortcuts import render
from . import models
from django.http import HttpResponse


def index(request):

    return render(request, 'honey_page.html')
