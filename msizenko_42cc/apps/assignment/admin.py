from django.contrib import admin
from django.contrib.auth.models import User
from msizenko_42cc.apps.assignment.models import UserProfile, Contact, RequestLog, DBLog


class UserProfileInline(admin.StackedInline):
    model = UserProfile

class ContactInline(admin.StackedInline):
    model = Contact
    extra = 1
    
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', )
    inlines = [UserProfileInline, ContactInline]
    
class RequestLogAdmin(admin.ModelAdmin):
    list_display = ('priority', 'date', 'path')
    
class DBLogAdmin(admin.ModelAdmin):
    list_display = ('date', 'module', 'name', 'action')
    
    
admin.site.unregister(User)    
admin.site.register(User, UserAdmin)
admin.site.register(RequestLog, RequestLogAdmin)
admin.site.register(DBLog, DBLogAdmin)
    