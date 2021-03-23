from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


#profil usera ma byc stworzony dla kazdego nowego uzytkowanika dlatego

@receiver(post_save,sender=User) #kiedy user jest zapisyany wyślij sygnał post_save
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User) #kiedy user jest zapisyany wyślij sygnał post_save
def save_profile(sender,instance,**kwargs):
    instance.profile.save()