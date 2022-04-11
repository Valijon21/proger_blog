from django.shortcuts import render

# Create your views here.
news = [
    {
        'title':'Birinchi habar',
        'text':'Habar bir',
        'date':'21.07.1993',
        'avtor':'Vlaijon'
    },
    {
        'title':'ikkinchi habar',
        'text':'Habar ikki',
        'date':'21.07.1993',
        'avtor':''
    },
    
]

def home(request):
    
    date = {
        'news':news,
        'title':'Bosh sahifa'
    }
    return render(request, 'blog/home.html', date)


def contact(request):
    
    return render(request,'blog/contact.html',{'title':'Contact haqida sahifa'})

