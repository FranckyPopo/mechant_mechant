from django.db import models

class NewsLater(models.Model):
    email = models.EmailField()
    
    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.email
  
class ContactUs(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    web_site = models.URLField()
    message = models.TextField()
    
    updated = models.fields.DateTimeField(auto_now=True)
    created = models.fields.DateTimeField(auto_now_add=True)
    deleted = models.fields.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.email
    