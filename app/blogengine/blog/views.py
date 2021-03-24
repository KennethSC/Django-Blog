from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    n = 'Bob'
    return render(request, 'blog/index.html', context={'name':n})