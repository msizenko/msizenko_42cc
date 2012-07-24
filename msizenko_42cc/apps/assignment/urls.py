from django.conf.urls.defaults import patterns, url
from django.views.generic import ListView
from msizenko_42cc.apps.assignment.models import RequestLog


urlpatterns = patterns('msizenko_42cc.apps.assignment.views',
    url(r'^$', 'index', name='assignment-index'),
    url(r'^log/$', ListView.as_view(
            queryset=RequestLog.objects.all()[:10],
            context_object_name='requests',
            template_name='assignment/log.html'), name='assignment-request-log'),                       
    url(r'^test/$', 'test'),
)