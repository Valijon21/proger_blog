from django.shortcuts import render
from .models import News
# Create your views here.

def home(request):
    
    date = {
        'news':News.objects.all(),
        'title':'Bosh sahifa'
    }
    return render(request, 'blog/home.html', date)


def contact(request):
    
    return render(request,'blog/contact.html',{'title':'Contact haqida sahifa'})

