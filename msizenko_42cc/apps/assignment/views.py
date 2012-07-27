from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth.models import User

from msizenko_42cc.apps.assignment.forms import UserForm, UserProfileForm, ContactFormSet

    
def index(request):
    person = User.objects.get_or_create(username='msizenko')[0]
    return render_to_response("assignment/index.html",
                              {'person': person},
                              context_instance=RequestContext(request))
    
@login_required    
def edit(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return redirect("/")
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        contact_set = ContactFormSet()
    return render_to_response("assignment/person_edit.html", {
                              'user_form': user_form,
                              'profile_form': profile_form,
                              'contact_set': contact_set})

    
    
    