import re
from django import forms
from lessons.models import Lessons
from .models import Profile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class UserRegForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta():
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            )


class ProfileForm(forms.ModelForm):
    phone = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={'class':'form-control'}))
    course = forms.MultipleChoiceField(label='Курс', widget=forms.CheckboxSelectMultiple, choices=(  
        ('python', 'Python'),
        ('unity3d', 'Unity 3D'),
        ('tech_svyazi', 'Технологии связи'),
    ))

    class Meta:
        model = Profile
        fields = ('phone', 'course')


class UserLogForm(AuthenticationForm):
        username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':'form-control'}))
        password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-control'}))




