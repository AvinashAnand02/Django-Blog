from django import forms
from .models import ContactMessage, Django

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        
class DjangoForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('Django', 'Django'),
        ('Networking', 'Networking'),
        ('Development', 'Development'),
    ]
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, label='Category')  # Add category field
    
    class Meta:
        model = Django
        fields = ['title', 'slug', 'author', 'category', 'content', 'status', 'image']  # Add category field to the form