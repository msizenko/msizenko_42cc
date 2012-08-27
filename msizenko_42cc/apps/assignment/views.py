import json
import itertools

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
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
    if request.method == 'POST':
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
        if request.is_ajax():
            return HttpResponse(json.dumps(response), mimetype='application/json')
    else:
        user_form = UserForm(instance=person)
        profile_form = UserProfileForm(instance=person.userprofile)
        contact_set = ContactFormSet(instance=person)
    return render(request,
                  "assignment/person_edit.html",
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'contact_set': contact_set})

@ensure_csrf_cookie
def request_log(request):
    LIST_SIZE = 10
    priority = request.GET.get('priority', '-priority')
    requests = RequestLog.objects.order_by(priority).all()[:LIST_SIZE]
    priority = 'priority' if priority == '-priority' else '-priority'
    return render(request,
                  'assignment/log.html',
                  {'requests': requests, 'priority': priority})

def priority_edit(request):
    if request.POST:
        try:
            log = RequestLog.objects.get(pk=request.POST.get('pk', None))
            log.priority = int(request.POST.get('priority', None))
            log.save();
            return HttpResponse()
        except ValueError:
            return HttpResponse(status='400')
    else:
        return HttpResponse(status='400')