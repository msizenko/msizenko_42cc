from django.db import models, utils
from django.contrib.auth.models import User
from annoying.fields import AutoOneToOneField
from django.db.models import signals


class UserProfile(models.Model):
    user = AutoOneToOneField(User, primary_key=True)
    date_of_birth = models.DateField(null=True, blank=True)
    bio = models.TextField()
    photo = models.ImageField(upload_to='profiles', null=True, blank=True)
    
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

class RequestLog(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=6)
    path = models.CharField(max_length=255)
    user = models.ForeignKey(User, blank=True,  null=True)
    user_agent = models.CharField(max_length=255)
    
    class Meta:
        ordering = ['-date']
        verbose_name = "logged request"
        
    def __unicode__(self):
        return '%s %s %s' %(self.date, self.method, self.path)
        
class DBLog(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    module = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    action = models.CharField(max_length=10)
    
    class Meta:
        ordering = ['-date']
    
    def __unicode__(self):
        return '%s %s %s' %(self.date, self.name, self.action)
        
def logging_update_create(instance, created, **kwargs):
    action = 'create' if created else 'update'
    logging(kwargs['sender'], action)
        
def logging_delete(sender, instance, **kwargs):    
    logging(sender, 'delete')
    
def logging(sender, action):
    skip_list = [DBLog, RequestLog]
    if sender not in skip_list:
        try:
            db_log = DBLog()
            db_log.module = sender.__module__
            db_log.name = sender.__name__
            db_log.action = action
            db_log.save()
        except utils.DatabaseError, e:
            return
    
signals.post_save.connect(logging_update_create)
signals.post_delete.connect(logging_delete)        
