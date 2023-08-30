from django import forms
from django.contrib.auth.models import User


class UpdateProfileInformation(forms.Form):
    first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'placeholder': 'Doe',
        'class': "mb-4 block p-3 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 shadow-sm focus:ring-primary-500 focus:border-primary-500"
    }))

    last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'placeholder': 'Joe',
        'class': "mb-4 block p-3 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 shadow-sm focus:ring-primary-500 focus:border-primary-500"
    }))

    phone = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'placeholder': '+92-3222222222',
        'class': "mb-4 block p-3 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 shadow-sm focus:ring-primary-500 focus:border-primary-500"
    }))

    area = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'placeholder': 'Model Town , Lahore',
        'class': "mb-4 block p-3 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 shadow-sm focus:ring-primary-500 focus:border-primary-500"
    }))

    address = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'placeholder': 'Street #1 .......',
        'class': "mb-4 block p-3 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 shadow-sm focus:ring-primary-500 focus:border-primary-500"
    }))

    landmark = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'placeholder': 'Gov College LHR',
        'class': "mb-4 block p-3 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 shadow-sm focus:ring-primary-500 focus:border-primary-500"
    }))
