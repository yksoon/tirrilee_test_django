from django import forms
from .models import Board

class BoardForm(forms.ModelForm):
    product = forms.CharField(label='Product', widget=forms.TextInput(
        attrs={'placeholder': '상품명을 입력해주세요.',
               'required': 'True'}
    ))
    price = forms.IntegerField(label='Price', widget=forms.NumberInput(
        attrs={'placeholder': '상품 가격을 입력해주세요.',
               'required': 'True'}
    ))
    image = forms.ImageField(label='Image', widget=forms.FileInput(
        attrs={'value': '사진첨부'}
    ))
    
    class Meta:
        model = Board
        fields = ('product', 'price', 'image')