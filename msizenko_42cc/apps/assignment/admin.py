from django.contrib import admin
from .models import UserProfile, Contact

class ContactInline(admin.StackedInline):
    model = Contact
    extra = 1

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', )
    inlines = [ContactInline]
    
admin.site.register(UserProfile, UserProfileAdmin)
    