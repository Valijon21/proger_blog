from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import Userreg

def register(request):
    if request.method == "POST":
        form = Userreg(request.POST)
        if form.is_valid():
            form.save() #formadagi malumotlarni bazaga saqlash
            username = form.cleaned_data.get('username')
            messages.success(request, f'foydalanuvchi {username} Ruyhatdan utdingiz kirish uchun login va parol ni kirtiin')
            return redirect('auth')
    else:  
        form = Userreg()
    return  render(request, 'users/registraion.html',{'form':form, 'title':"Ruyhatga olish"})


def profile(request):
    return render(request, 'users/profile.html')