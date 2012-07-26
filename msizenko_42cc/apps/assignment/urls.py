from django.conf.urls.defaults import patterns, url
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView
from msizenko_42cc.apps.assignment.models import RequestLog


urlpatterns = patterns('msizenko_42cc.apps.assignment.views',
    url(r'^$', 'index', name='assignment-index'),
    url(r'^request-log/$', ListView.as_view(
            queryset=RequestLog.objects.all()[:10],
            context_object_name='requests',
            template_name='assignment/log.html'),
        name='assignment-request-log'),
)

urlpatterns += patterns('django.contrib.auth.views',
    url(r'^login/$', 'login', {
            'template_name': 'assignment/login.html',
            'authentication_form': AuthenticationForm},
        name='assignment-login'),
    url(r'^logout/$', 'logout', {'next_page': '/'}, name='assignment-logout'),
)