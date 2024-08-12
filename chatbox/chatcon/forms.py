# forms.py
from django import forms
from .models import User, Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('text',)
    def clean_text(self):
        text = self.cleaned_data.get('text')
        if len(text) < 1:
            raise forms.ValidationError('Message cannot be empty')
        return text        

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError('Password must be at least 8 characters')
        return password

class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=255, label='Confirm Password')

    class Meta:
        model = User
        fields = ('username', 'password')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match')
        return cleaned_data
    