from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth.models import User

from msizenko_42cc.apps.assignment.forms import UserForm, UserProfileForm, ContactFormSet

    
def index(request):
    person = User.objects.get_or_create(username='admin')[0]
    return render_to_response("assignment/index.html",
                              {'person': person},
                              context_instance=RequestContext(request))
    
@login_required    
def edit(request):
    person = User.objects.get(pk=request.user.pk)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=person)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=person.userprofile)
        contact_set = ContactFormSet(request.POST, instance=person)
        if user_form.is_valid() and profile_form.is_valid() and contact_set.is_valid():
            user_form.save()
            profile_form.save()
            contact_set.save()
            return redirect("/")
    else:
        user_form = UserForm(instance=person)
        profile_form = UserProfileForm(instance=person.userprofile)
        contact_set = ContactFormSet(instance=person)
    return render_to_response("assignment/person_edit.html", {
                              'user_form': user_form,
                              'profile_form': profile_form,
                              'contact_set': contact_set},
                               context_instance=RequestContext(request))


    
    
    