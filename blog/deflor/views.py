from django.shortcuts import render
from deflor.models import *


def index(request):
    women = Women.objects.all()
    return render(request, "deflor/index.html", {'title': "Home page", 'womens': women})
