from django.forms import ModelForm
from django.forms.models import inlineformset_factory    
from django.contrib.auth.models import User
from msizenko_42cc.apps.assignment.models import UserProfile, Contact


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)
        
ContactFormSet = inlineformset_factory(User, Contact)        
        
        
        
