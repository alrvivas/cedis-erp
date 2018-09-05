from django import forms
from .models import Route, Cedis

class routeForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ('__all__')
