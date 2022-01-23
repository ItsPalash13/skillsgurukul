from django import forms
from django.forms import ModelForm
from .models import Email_list

class Form(ModelForm):
   class Meta:
      model=Email_list
      fields = ['name','email','message']

      widget={
         "name":forms.TextInput(attrs={'class':'pt1inp'}),
         "email":forms.TextInput(attrs={'class':'pt1inp'}),
         "message":forms.TextInput(attrs={'class':'pt1inp'})
      }
class MessageForm(forms.Form):
   name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your name..','id':'pt1inp'}))
   email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your email..','id':'pt1inp'}))
   message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Enter your message...','id':'txtarmsg'}))
   def save(self):
      data=self.data
      modelRef=Email_list(name=data['name'],email=data['email'],message=data['message'])
      modelRef.save()

