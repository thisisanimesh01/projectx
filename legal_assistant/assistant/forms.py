from django import forms
from .models import LegalDocument

class UploadForm(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['file']
