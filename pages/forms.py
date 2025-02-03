from django import forms
from pages.models import ContactForm

class SendForm(forms.ModelForm):
    class Meta:
        model = ContactForm

        fields = ['name', 'email', 'subject', 'messages']
        labels = {
            'name': 'Name and Lastname',
            'email': 'E-Mail',
            'subject': 'Subject',
            'messages': 'Message'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name and Lastname'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-Mail'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'messages': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message', 'rows': '5'}),
        }
        error_messages = {
            'name': {
                'required': 'Name and Lastname is required'
            },
            'email': {
                'required': 'E-Mail is required',
                'invalid': 'Please enter a valid E-Mail'
            },
            'subject': {
                'required': 'Subject is required'
            },
            'messages': {
                'required': 'Message is required'
            }
        }

