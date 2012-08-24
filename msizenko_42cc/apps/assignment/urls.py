from django.conf.urls.defaults import patterns, url
from django.contrib.auth.forms import AuthenticationForm
from msizenko_42cc.apps.assignment.views import RequestLogListView


urlpatterns = patterns('msizenko_42cc.apps.assignment.views',
    url(r'^$', 'index', name='assignment-index'),
    url(r'^person-edit/$', 'edit', name='assignment-person-edit'),                       
    url(r'^request-log/$', RequestLogListView.as_view(), name='assignment-request-log'),
)

urlpatterns += patterns('django.contrib.auth.views',
    url(r'^login/$', 'login', {
            'template_name': 'assignment/login.html',
            'authentication_form': AuthenticationForm},
        name='assignment-login'),
    url(r'^logout/$', 'logout', {'next_page': '/'}, name='assignment-logout'),
)
