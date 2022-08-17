import random
from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    return render(request, 'index.html')

def dinner(request, name):
    menus = [{"name":'족발', "price": 30000}, {"name":'햄버거', "price": 10000}, {"name":'치킨', "price": 20000}, {"name":'초밥', "price": 18000},]
    pick =random.choice(menus)
    articles = Article.objects.order_by('-pk')
    context = {
        'pick': pick,
        'name': name,
        'menus': menus,
        'articles':articles,
    }
    return render(request, 'dinner.html', context)

def review(request):
    return render(request, 'review.html')

def create_review(request):
    content = request.POST.get('content')
    title = request.POST.get('title')
    
    article = Article(title=title, content=content)
    article.save()
    
    return redirect ('/articles/dinner/무언가/')