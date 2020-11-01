from .models import Profile, Neighbourhood, Business ,Post
from django import forms
from django.contrib.auth.forms import AuthenticationForm
class UpdateProfile(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['bio','profilepic','email'] 
        exclude=['user']   


class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ['Neighborhood','Neighborhood_location', 'population','police_no','hospital_no']

class BusinessForm(forms.ModelForm):
   
    class Meta:
        model = Business
        fields = ['image','project', 'email']

class PostMessageForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message']