from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import Userreg
from django.contrib.auth.decorators import login_required
from .forms import Userreg, ProfileImage, UserUpdateForm


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

# funksiyaga dekorator qushamiz
@login_required
def profile(request):
     if request.method == "POST":
        img_profile = ProfileImage(request.POST, request.FILES, instance=request.user.profile)
        update_user = UserUpdateForm(request.POST, instance=request.user)
        if update_user.is_valid() and img_profile.is_valid():
            update_user.save()
            img_profile.save()
            messages.success(request, f'Akkaunt malumotlariz yangilandi')
            
            return redirect('profile')
     else:
        img_profile = ProfileImage(instance=request.user.profile)
        update_user = UserUpdateForm(instance=request.user)
        
     data = {
        'img_profile': img_profile,
        'update_user': update_user
     }
     return render(request, 'users/profile.html', data)