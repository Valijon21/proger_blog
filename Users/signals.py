from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User) # bu sender foydalanuvchi tablitsa tushsa post_save signal ishga tushadi
def create_profile(sender, instance, created, **kwargs):
    #profila tablitsasa malumot kiritish funksiyasi
    if created: # agar yangi obyekt yaratilsa profile tablsitsada yangi zapis yaratiladi
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)

   # '''User tablitsasi yangilansa profile ham yangilsansin function'''
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
    