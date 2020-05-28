from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Member

class SignupForm(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'placeholder' : '이메일을 입력해주세요.',
               'required' : 'True',
               }
    ))
    nickname = forms.CharField(label="Nickname", max_length=50,
                               widget=forms.TextInput(
                                   attrs={'placeholder': '티릴리에서 사용할 닉네임을 입력해주세요',
                                          'required': 'True',
                                          }
                               ))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(
                                   attrs={
                                       'plaeholder': '숫자,영문,특수문자 포함 12자',
                                       'pattern': '(?=^.{8,12}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$',
                                       'required': 'True',
                                       }
                               ))
    phone = forms.IntegerField(label='Phone',
                               widget=forms.TextInput(
                                   attrs={
                                       'placeholder': '"-"제외, 숫자만 입력해주세요.',
                                       'pattern': '[0-1]{3}[0-9]{3,4}[0-9]{4}',
                                       'required': 'True',
                                       }
                               ))
    
    class Meta:
        model = Member
        fields = ("email", "nickname", "password", "phone")

