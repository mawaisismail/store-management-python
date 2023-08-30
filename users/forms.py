from django import forms
from django.contrib.auth.models import User


class UserForgetPassword(forms.Form):
    email = forms.EmailField(max_length=200, widget=forms.TextInput(attrs={
        'class': "bg-gray-50 mb-6 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"
    }))
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "bg-gray-50 mb-6 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"}))

    new_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "bg-gray-50 mb-6 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"}))

    confirm_new_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "bg-gray-50 mb-6 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"}))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            user = User.objects.get(email=email)
            print(user)
        except User.DoesNotExist:
            raise forms.ValidationError("User Does not exist")

    def clean_confirm_new_password(self):
        confirm_new_password = self.cleaned_data.get('confirm_new_password')
        new_password = self.cleaned_data.get('new_password')
        if confirm_new_password != new_password:
            raise forms.ValidationError("Password not match")

    def clean_new_password(self):
        old_password = self.cleaned_data.get('old_password')
        confirm_new_password = self.cleaned_data.get('confirm_new_password')
        if old_password != confirm_new_password:
            raise forms.ValidationError("Password not match")
