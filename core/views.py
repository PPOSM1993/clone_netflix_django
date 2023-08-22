from django.shortcuts import render, redirect
from .models import *
from django.views import View
from django.contrib.auth.decorators import login_required
from  django.utils.decorators  import method_decorator

# In this file, we gonna to create our views, which will be rendered from python file to html, and will be seen by the user

class Home(View):
    def get(self, request, **kwargs):
        if request.user.is_authenticated:
            return redirect('core:profile_list')
        return render(request, 'index.html')

@method_decorator(login_required, name='dispatch')
class ProfileList(View):
    def get(self, request, **kwargs):
        profiles =request.user.profile.all()
        return render(request, 'profileList.html',{
            'profiles': profiles
        }
    )


class ProfileCreate(View):
    pass