'''
Created on 25 Nov 2023

@author: mpayen
'''

from django import forms
from website.models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ("nom", "email", "sujet", "contenu")
        
    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['nom'].required = True
        self.fields['email'].required = True
        self.fields['sujet'].required = False
        self.fields['contenu'].required = True