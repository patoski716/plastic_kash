from django.forms import ModelForm
from django import forms
from .models import *


class VendorForm(ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'