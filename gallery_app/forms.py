from django import forms
from gallery_app.models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ["title", "image"]