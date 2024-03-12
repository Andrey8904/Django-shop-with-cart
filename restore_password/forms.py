from django import forms

class RestorePasswordForm(forms.Form):
    user_email = forms.EmailField(label='E-Mail', widget=forms.TextInput(attrs={'class': 'form-control'}))

class RestoreCodeForm(forms.Form):
    user_code = forms.IntegerField(widget=forms.TextInput())

class NewPasswordForm(forms.Form):
    user_password = forms.CharField(widget=forms.PasswordInput(), label='Password')
    user_password_repeat = forms.CharField(widget=forms.PasswordInput(), label='Password repeat')


