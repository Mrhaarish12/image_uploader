from django import forms
from .models import Image

class ImageForm(forms.ModelFrom):
    class Meta:
        model = Image
        fields = '__all__'