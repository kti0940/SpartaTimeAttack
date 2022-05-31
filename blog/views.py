from django.shortcuts import render, redirect

# Create your views here.

def blog(request):
    if request.method == 'GET':
        return render(request, 'blog/new.html')
