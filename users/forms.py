from django import forms


class UserForgetPassword(forms.Form):
    Email = forms.EmailField(max_length=200, widget=forms.TextInput(attrs={
        'class': "bg-gray-50 mb-6 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"
    }))
    Password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "bg-gray-50 mb-6 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"}))

    Confirm_Password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "bg-gray-50 mb-6 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"}))
