from django import forms
from app.models import Product
from django.contrib.auth.models import User
import account.forms

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        def clean(self):
            email = self.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                raise form.ValidationError('Пользователь с такой электронной почтой уже зарегистрирован')

class SignupForm(account.forms.SignupForm):
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        del self.fields["username"]

class CartForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'img', 'price']
        widgets = {
            'name': forms.HiddenInput(),
            'img': forms.HiddenInput(),
            'price': forms.HiddenInput()
        }

class OrderForm(forms.Form):
    name = forms.CharField()

    widgets = {
        'name': forms.HiddenInput(),
    }
