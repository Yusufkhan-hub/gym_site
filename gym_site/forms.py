from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from .models import feedback

class signupForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','email']

# class galleryForm(ModelForm):

#     class Meta:
#         model = gallery
#         fields = ['photo']

class feedbackForm(ModelForm):

    class Meta:
        model = feedback
        fields = ['name','email','message']