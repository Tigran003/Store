from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from  .models import  User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'autofocus': True,
                                      'class': 'form-control',
                                      'placeholder': 'Enter your username'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password',
                                          'class': 'form-control',
                                          'placeholder': 'Enter your password'})

    )
    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        )

    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField()
    password2 = forms.CharField()


    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Enter your  name',
    #         }
    #     )
    # )
    # last_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Enter your last name',
    #         }
    #     )
    # )
    # username = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Enter your username',
    #         }
    #     )
    # )
    # email = forms.EmailField(
    #     widget=forms.EmailInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Enter your email address',
    #         }
    #     )
    # )
    # password1 = forms.CharField(
    #     widget=forms.PasswordInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Enter your password',
    #         }
    #     )
    # )
    # password2 = forms.CharField(
    #     widget=forms.PasswordInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Enter your password',
    #         }
    #     )
    # )

class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'image',
            'first_name',
            'last_name',
            'username',
            'email',)

    image = forms.ImageField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()