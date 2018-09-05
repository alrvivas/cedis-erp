from django import forms
from .models import Client, Employee

class clientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('__all__')


class employeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('__all__')