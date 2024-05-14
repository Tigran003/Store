from django.shortcuts import render
from django.http import HttpResponse
from goods.models import  Category

def index(request) -> HttpResponse:



    context = {
        'title':'Home - Main',
        'content':'Furniture store HOME',

    }
    return  render(request, 'main/index.html',context)

def about(request) -> HttpResponse:
    context = {
        'title': 'Home - About us',
        'content': 'About us',
        'text_on_page': 'Text about why this store is so cool '

    }
    return render(request, 'main/about.html', context)
