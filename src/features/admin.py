from django.contrib import admin

from features.models import NewsLater, ContactUs

@admin.register(NewsLater)
class NewsLater(admin.ModelAdmin):
    list_display = ["email", "created"]
    
@admin.register(ContactUs)
class ContactUs(admin.ModelAdmin):
    list_display = ["name", "email", "message", "created"]
    
    
    