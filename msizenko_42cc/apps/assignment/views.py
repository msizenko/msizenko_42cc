from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User

    
def index(request):
    person = User.objects.get_or_create(username='msizenko')[0]
    contacts = person.contact_set.all()
    return render_to_response("assignment/index.html",
                              {'person': person, 'contacts': contacts},
                              context_instance=RequestContext(request))
    