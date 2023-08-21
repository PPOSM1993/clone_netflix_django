from django.shortcuts import render
from .models import *
from django.views import View

# In this file, we gonna to create our views, which will be rendered from python file to html, and will be seen by the user

class Home(View):
    def get(self, request, **kwargs):
        return render(request, 'index.html')
