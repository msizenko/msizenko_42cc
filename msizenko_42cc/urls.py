from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('',
    url('', include('msizenko_42cc.apps.assignment.urls'))
)
