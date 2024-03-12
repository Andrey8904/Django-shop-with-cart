from django import forms


class RegisterUserForm(forms.Form):
    user_name = forms.CharField(max_length=50, label='Name')
    user_email = forms.EmailField(label='E-Mail')
    user_password = forms.CharField(widget=forms.PasswordInput(), label='Password')
    user_password_repeat = forms.CharField(widget=forms.PasswordInput(), label='Password repeat')
    user_agree = forms.BooleanField(label='Rules')

class ActivateCodeForm(forms.Form):
    activate_code = forms.IntegerField(label='Введите код', widget=forms.TextInput())

class ActivateEmailForm(forms.Form):
    user_email = forms.EmailField(label='E-Mail', widget=forms.TextInput(attrs={'class': 'form-control'}))


class LoginUserForm(forms.Form):
    user_email = forms.EmailField(label='E-Mail', widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Password')
