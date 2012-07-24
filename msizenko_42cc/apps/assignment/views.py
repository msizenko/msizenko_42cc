from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User


def test(request):
    """
    Test page.
    """
    return render_to_response("assignment/test.html")
    
def index(request):
    user = User.objects.get_or_create(username='msizenko')[0]
    contacts = user.contact_set.all()
    return render_to_response("assignment/index.html", {'user': user, 'contacts': contacts}, context_instance=RequestContext(request))

    