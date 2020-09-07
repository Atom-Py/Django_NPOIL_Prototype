from django import forms
from django.contrib.auth.models import User
from .models import PersonalInfo, Requisition, Message, Response

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)
    check = forms.BooleanField(label='Согласие на обработку персональных данных (согласно ФЗ №152-ФЗ)')

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password2']

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = ('phone', 'juristical_address', 'agent_company', 'docs_client')

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('subject', 'message')