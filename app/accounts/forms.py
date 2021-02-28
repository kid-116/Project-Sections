from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Account
from django.contrib.auth import authenticate


class AccountSignupForm(UserCreationForm):

    email = forms.EmailField(max_length=60)
    username = forms.CharField(help_text="*Cannot be changed once fixed")
    role = forms.ChoiceField(help_text="*Cannot be changed once fixed", choices=Account.Role.choices)

    class Meta:
        model = Account
        fields = [
            'email',
            'username',
            'role',
            'password1',
            'password2',
        ]


class AccountAuthenticationForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = [
            'email',
            'password'
        ]    

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Invalid login credentials")


class AccountUpdateForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = [
            'email',
        ]

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = Account.objects.exclude(pk = self.instance.pk).get(email = email)
            except:
                return email
            raise forms.ValidationError('Email "%s" is already in use' %email)
