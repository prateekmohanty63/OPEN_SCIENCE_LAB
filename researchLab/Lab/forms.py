from dataclasses import field
from pickle import TRUE
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# user creation form

class NewuserForm(UserCreationForm):
    email=forms.EmailField(required=True)


    class Meta:
        model=User
        fields=("username","email","password1","password2")
        widgets={
            'username':forms.TextInput(attrs={
                'class':"form-controls",
                'style':'max-width:300px;padding:1.0rem',
                
                'placeholder':'Username'
            }
            
            ),
            'email':forms.EmailInput(attrs={
                'class':'form-control',
                'style':'max-width:300px;padding:1rem',
                'placeholder':'Email'
            }
            )
        }
    
    def save(self,commit=True):
        user=super(NewuserForm,self).save(commit=False)
        user.email=self.cleaned_data['email']

        if commit:
            user.save()
        return user