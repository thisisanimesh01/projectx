from django import forms
from .models import Document


class UploadForm(forms.ModelForm):
    question = forms.CharField(required=False)

    class Meta:
        model = Document
        fields = ['file']