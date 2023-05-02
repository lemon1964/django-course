from django.forms import forms

class Gallery_Upload_Forms(forms.Form):
    image = forms.FileField()  # image берем из html