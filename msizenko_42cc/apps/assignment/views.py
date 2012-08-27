import json
import itertools

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib.auth.models import User
from msizenko_42cc.apps.assignment.models import RequestLog

from msizenko_42cc.apps.assignment.forms import UserForm, UserProfileForm, ContactFormSet


def index(request):
    person = User.objects.get_or_create(username='admin')[0]
    return render(request,
                  "assignment/index.html",
                  {'person': person})

@login_required    
def edit(request):
    person = User.objects.get(pk=request.user.pk)
    if request.is_ajax() and request.method == 'POST':
        user_form = UserForm(request.POST, instance=person)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=person.userprofile)
        contact_set = ContactFormSet(request.POST, instance=person)
        response = {}
        if user_form.is_valid() and profile_form.is_valid() and contact_set.is_valid():
            user_form.save()
            profile_form.save()
            contact_set.save()
            response['success'] = True
        else:
            errors = dict(user_form.errors.items() + profile_form.errors.items())            
            for i, dict_errors in enumerate(contact_set.errors):
                for field in dict_errors: 
                    key = 'contact_set-'+ str(i) + '-' + field
                    errors[key] = dict_errors[field]
            response['errors'] = errors
        return HttpResponse(json.dumps(response), mimetype='application/json')
    else:
        user_form = UserForm(instance=person)
        profile_form = UserProfileForm(instance=person.userprofile)
        contact_set = ContactFormSet(instance=person)
        return render(request,
                      "assignment/person_edit.html", {
                          'user_form': user_form,
                          'profile_form': profile_form,
                          'contact_set': contact_set})

class RequestLogListView(ListView):
    LIST_SIZE = 10
    PRIORITY = 0

    context_object_name='requests'
    template_name='assignment/log.html'

    def get_queryset(self):
        priority = self.request.GET.get('priority', self.PRIORITY)
        priorited = RequestLog.objects.filter(priority=priority).all()[:self.LIST_SIZE]
        general = RequestLog.objects.exclude(priority=priority).all()[:self.LIST_SIZE - priorited.count()]
        return itertools.chain(priorited, general)
