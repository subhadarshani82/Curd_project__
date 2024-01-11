from django.shortcuts import render
from .models import Login

# Create your views here.
def login(request):
    user=Login.objects.all()
    return render(request,'login.html',{'user':user})
