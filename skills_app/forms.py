from django import forms
from django.forms import ModelForm
from .models import Updates

class UpdatesForm(ModelForm):
   class Meta:
      model=Updates
      fields = ['email']

      widget={
         "email":forms.TextInput(attrs={'class':'pt1inp'})
      }
class UpdatesForm1(forms.Form):
   email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your email...','id':'pt1inp'}))
   def save(self):
      data=self.data
      modelRef=Updates(email=data['email'])
      modelRef.save()

