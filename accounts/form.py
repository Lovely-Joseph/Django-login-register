# from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
# Creating forms
class CreateUserForm(UserCreationForm):
    # Describing the table relation 
    class Meta:
        model=User
        # fields='__all__'
        fields=['username','email','password1','password2']
