from django import forms
from captcha.fields import ReCaptchaField
from ap.models import *
from .models import *

class FormWithCaptcha(forms.Form):
    captcha = ReCaptchaField()


class Video_form(forms.ModelForm):
    class Meta:
        model = Video
        fields = ("caption","video")