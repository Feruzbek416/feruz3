from django.shortcuts import render
from .models import *
from .forms import FormWithCaptcha
from .forms import Video_form
# Create your views here.

def VideoView(request):
    videos = Video.objects.all()
    if request.method == "POST":
        form = Video_form(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = Video_form()
    return render(request, 'ap/video.html',{'videos':videos,"form":form})



def PhoneView(request):
    phone = Add_Model.objects.all()
    return render(request, 'ap/phone.html',{'phone':phone})

def Repatcha(request):
    recaptcha = FormWithCaptcha()
    return render(request, 'ap/recaptcha.html',{'recaptcha':recaptcha})