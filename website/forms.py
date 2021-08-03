from django import forms
from .models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['mesage', 'email', 'phone']
        labels = {'mesage': 'Message', 'email': 'Email', 'phone': 'Phone'}
        widget = {'mesage': forms.Textarea(attrs={'cols'    : 80})}
