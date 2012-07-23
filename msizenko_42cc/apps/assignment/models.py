from django.db import models
from django.contrib.auth.models import User
from annoying.fields import AutoOneToOneField


class UserProfile(models.Model):
    user = AutoOneToOneField(User, primary_key=True)
    date_of_birth = models.DateField(blank=True)
    bio = models.TextField()
    
class Contact(models.Model):
    TYPE_CHOICES = (
        ('JB', 'jabber'),
        ('SK', 'skype'),
        ('TW', 'twitter')
    )
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    value = models.CharField(max_length=254)
    user = models.ForeignKey(User)
    
    class Meta:
        verbose_name = "contact"
        
    def __unicode__(self):
        return "%s: %s" % (self.get_type_display(), self.value)
    
    

    
