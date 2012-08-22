from django import template
from django.core import urlresolvers


register = template.Library()

def edit_link(obj, title=None):
    viewname  = "admin:%s_%s_change" % (obj._meta.app_label, obj._meta.object_name)
    url = urlresolvers.reverse(viewname.lower(), args=(obj.pk,))
    title = title if title is not None else 'admin'
    return {'link': url, 'title': title}

    
register.inclusion_tag('assignment/edit_link.html')(edit_link)        
