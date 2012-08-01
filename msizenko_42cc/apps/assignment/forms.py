from django import forms
from django.forms.models import inlineformset_factory    
from django.contrib.auth.models import User
from msizenko_42cc.apps.assignment.models import UserProfile, Contact


class CalendarWidget(forms.DateInput):
    class Media:
        css = { 'all': ('css/jquery-ui-1.8.22.custom.css', ) }
        js = ('js/jquery-ui-1.8.22.custom.min.js', )

    def __init__(self, *args, **kwargs):
        kwargs['attrs'] = {'class' : 'datepicker'}
        super(CalendarWidget, self).__init__(*args, **kwargs)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)
        widgets = {'date_of_birth': CalendarWidget}
        
ContactFormSet = inlineformset_factory(User, Contact, max_num=len(Contact.TYPE_CHOICES), extra=1)        
