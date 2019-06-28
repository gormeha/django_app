from django import forms
from myapp.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['client', 'product', 'num_units']

    client = forms.ModelChoiceField(queryset=Client.objects.all(), label='Client Name')
    product = forms.ModelChoiceField(queryset=Product.objects.all(), label='Product Name')
    num_units = forms.IntegerField(label='Quantity')


class InterestForm(forms.Form):
    interested_in = forms.ChoiceField(widget=forms.RadioSelect, choices=[(1,'Interested'),(0, 'Not interested')], label='Intrested')
    quantity = forms.IntegerField(initial=1, label='Quantity')
    comments = forms.CharField(widget=forms.Textarea, required=False, label='Additional Comments')


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    username = forms.CharField(max_length=30, required=True)
    profile_pic = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2' )

#class LoginForm(forms.ModelForm):
#    username = forms.CharField(max_length=20, required=True, label='User Name')
#    password = forms.CharField(widget=forms.PasswordInput())#
#
#    class Meta:
#        model = Client
