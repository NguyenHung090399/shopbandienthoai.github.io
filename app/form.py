from django import forms
import re # kiem tra bieu thuc chinh quy
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class RegistrationForm(forms.Form) : 
    username    = forms.CharField(label='Tên đăng nhập' , max_length=30 , widget=forms.TextInput(attrs={'class':'form-control'}))
    email       = forms.EmailField(label='Email' ,  widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1   = forms.CharField(label='Mật khẩu' , widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2   = forms.CharField(label='Nhập lại mật khẩu' , widget=forms.PasswordInput(attrs={'class':'form-control'}))
#Ham kiem tra pw
    def clear_password2(self) : # phuong thuc kiem tra du lieu nhap lai mat khau
        if 'password1' in self.cleaned_data : # kiem tra xem pw 1 da duoc nhap chua 
            #lay ra
            password1 = self.cleaned_data['password1'] # lay thong tin cua pw1 va pw2
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1 : 
                return password2
        raise forms.ValidationError('Mật khẩu không khớp!')
#ham kiem tra username
    def clear_usename(self) : 
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$' , username): # r'^\W+$' : cac ki tu thuong
            raise forms.ValidationError('Tên tài khoản không được chứa kí tự đặc biệt')
        try:
            User.objects.get(username = username)
        except ObjectDoesNotExist : # khong co username nhu vay 
            return username
        raise forms.ValidationError('Tài khoản đã tồn tại')
    