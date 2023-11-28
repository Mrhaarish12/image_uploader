from django import forms
from .models import Image

#form
class ImageForm(forms.ModelFrom):
    class Meta:
        model = Image
        fields = '__all__'
        labels = {'photo': ''}