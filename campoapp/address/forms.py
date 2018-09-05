from django import forms
from django.forms.models import inlineformset_factory
from .models import Address
from person.models import Client

class addressForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ()

AddressFormSet = inlineformset_factory(Client, Address,form=addressForm, extra=1)