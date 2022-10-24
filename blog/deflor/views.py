from django.shortcuts import render
from deflor.models import *

menu = [{'title': 'О Сайте', 'url_name': 'about'},
        {'title': 'Обратная связь', 'url_name': 'feedback'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        ]


def index(request):
    women = Women.objects.all()
    return render(request, "deflor/index.html", {'menu': menu, 'womens': women})


def about(request):
    return render(request, "deflor/about.html", {'menu': menu})


def feedback(request):
    return render(request, "deflor/feedback.html", {'menu': menu})


def add_page(request):
    return render(request, "deflor/new_text.html", {'menu': menu})

def login(request):
    return render(request, "deflor/login.html", {'menu': menu})
def show_actor(request, post_number):
    women = Women.objects.get(pk = post_number)
    return render(request, "deflor/show.html", {'menu': menu,'womens': women})
