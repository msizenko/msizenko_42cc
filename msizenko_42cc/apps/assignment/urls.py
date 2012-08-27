from django.conf.urls.defaults import patterns, url
from django.contrib.auth.forms import AuthenticationForm


urlpatterns = patterns('msizenko_42cc.apps.assignment.views',
    url(r'^$', 'index', name='assignment-index'),
    url(r'^person-edit/$', 'edit', name='assignment-person-edit'),                       
    url(r'^request-log/$', 'request_log', name='assignment-request-log'),
    url(r'^request-log/edit/$', 'priority_edit', name='assignment-priority-edit'),
)

urlpatterns += patterns('django.contrib.auth.views',
    url(r'^login/$', 'login', {
            'template_name': 'assignment/login.html',
            'authentication_form': AuthenticationForm},
        name='assignment-login'),
    url(r'^logout/$', 'logout', {'next_page': '/'}, name='assignment-logout'),
)
