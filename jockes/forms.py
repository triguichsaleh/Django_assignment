from django import forms
from django.contrib.auth.models import User
from .models import Jocke

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return confirm_password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user





class JockeForm(forms.ModelForm):
    class Meta:
        model = Jocke
        fields = ['question', 'answer']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['question'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your question'})
        self.fields['answer'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your answer'})
