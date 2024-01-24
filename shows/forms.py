import re

from django import forms
from django.core.exceptions import ValidationError
from .models import Show

TITLE_REGEX = re.compile(r'^[A-Za-z0-9 ]+$')

# Two different custom forms since I want the UpdateView to only have 'title' field to edit.
class CreateShowForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = '__all__'

    def clean_title(self):
        title = self.cleaned_data.get('title', '')
        if len(title) < 2:
            raise ValidationError('Title must be at least 2 characters long')
        if not re.match(TITLE_REGEX, title):
            raise ValidationError('Title too complex bruh')
        
        return title

    
    def clean_network(self):
        network = self.cleaned_data.get('network', '')
        if len(network) < 3:
            raise ValidationError('Network must be at least 3 characters long')
        if not re.match(TITLE_REGEX, network):
            raise ValidationError('Network too complex bruh')
        return network
    
    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        if description == '':
            return description
        elif len(description) < 10:
            raise ValidationError('Description must be at least 10 characters long')
        return description
    
    
# Only includes one field compared to the CreateForm that includes all
class UpdateShowForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = ['title', 'description']

    def clean_title(self):
        title = self.cleaned_data.get('title', '')
        if len(title) < 2:
            raise ValidationError('Title must be at least 2 characters long')
        if not re.match(TITLE_REGEX, title):
            raise ValidationError('Title too complex bruh')
        
        return title

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        if description == '':
            return description
        elif len(description) < 10:
            raise ValidationError('Description must be at least 10 characters long')
        return description