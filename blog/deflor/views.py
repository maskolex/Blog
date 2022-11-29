from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from deflor.forms import AddWomen
from deflor.models import *

menu = [{'title': 'О Сайте', 'url_name': 'about'},
        {'title': 'Обратная связь', 'url_name': 'feedback'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        ]


class Index(ListView):
    model = Women
    template_name = "deflor/index.html"
    context_object_name = 'womens'

    def get_context_data(self, **kwargs):
        # Возвращаем список сформированных обьектов
        context = super().get_context_data(**kwargs)
        # Добавляем нужные элементы
        context['category'] = Category.objects.all()
        context['menu'] = menu
        context['title'] = "Главная страница"
        return context

    def get_queryset(self):
        return Women.objects.filter(is_published=True)


def about(request):
    category = Category.objects.all()
    return render(request, "deflor/about.html", {'menu': menu, 'category': category})


def feedback(request):
    category = Category.objects.all()
    return render(request, "deflor/feedback.html", {'menu': menu, 'category': category})


def add_page(request):
    category = Category.objects.all()
    if request.method == 'POST':
        forms = AddWomen(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('home_page')
    else:
        forms = AddWomen()

    return render(request, "deflor/new_text.html", {'menu': menu, 'category': category, 'forms': forms})


def login(request):
    category = Category.objects.all()
    return render(request, "deflor/login.html", {'menu': menu, 'category': category})


# class ShowActor(DetailView):
#     model = Women
#     template_name = "deflor/show.html"
    # context_object_name = "womens"
    # def get_context_data(self, **kwargs):
    #     # Возвращаем список сформированных обьектов
    #     context = super().get_context_data(**kwargs)
    #     # Добавляем нужные элементы
    #     context['category'] = Category.objects.all()
    #     context['menu'] = menu
    #     context['title'] = Category.objects.get(slug=self.kwargs["slug"]).name
    #     # context['cat_select'] = context['womens'][0].cat_id
    #     return context

def show_actor(request, post_slug):
    women = get_object_or_404(Women, slug=post_slug)
    category = Category.objects.all()
    cat_select = women.cat_id
    context = {
        'menu': menu,
        'womens': women,
        'category': category,
        'cat_select': cat_select
    }

    return render(request, "deflor/show.html", context=context)


class ShowCategory(ListView):
    model = Women
    template_name = "deflor/category.html"
    context_object_name = 'womens'

    def get_context_data(self, **kwargs):
        # Возвращаем список сформированных обьектов
        context = super().get_context_data(**kwargs)
        # Добавляем нужные элементы
        context['category'] = Category.objects.all()
        context['menu'] = menu
        context['title'] = Category.objects.get(slug=self.kwargs["cat_slug"]).name
        context['cat_select'] = context['womens'][0].cat_id
        return context

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs["cat_slug"], is_published=True)