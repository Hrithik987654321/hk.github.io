from django.contrib import admin
from authapp.models import phpgallery,LinuxGallery,SaseGallery,StatisticsGallery,DaaGallery
# Register your models here.
from .models import ContactMessage

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject','message','created_at']

admin.site.register(ContactMessage, ContactMessageAdmin)

admin.site.register(phpgallery)
admin.site.register(LinuxGallery)
admin.site.register(StatisticsGallery)
admin.site.register(SaseGallery)
admin.site.register(DaaGallery)
