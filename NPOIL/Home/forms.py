from django import forms
from django.contrib.auth.models import User
from Cabinet.models import Order

class BuyForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('volume', 'address')