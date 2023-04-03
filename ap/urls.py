
from django.urls import path
from .views import *

urlpatterns = [
    path('',VideoView,name='video'),
    path('phone/',PhoneView,name='phone'),
    path('recaptcha/',Repatcha,name='recaptcha'),
]