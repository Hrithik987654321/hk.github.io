from django.db import models
from datetime import datetime

# Create your models here.
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.subject
    
class phpgallery(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='pdfs')
    timeStamp = models.DateTimeField(default=datetime.now, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.timeStamp = datetime.now()
        return super(phpgallery, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class LinuxGallery(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='linux_pdfs')
    timeStamp = models.DateTimeField(default=datetime.now, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.timeStamp = datetime.now()
        return super(LinuxGallery, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class SaseGallery(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='sase_pdfs')
    timeStamp = models.DateTimeField(default=datetime.now, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.timeStamp = datetime.now()
        return super(SaseGallery, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class DaaGallery(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='daa_pdfs')
    timeStamp = models.DateTimeField(default=datetime.now, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.timeStamp = datetime.now()
        return super(DaaGallery, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class StatisticsGallery(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='statistics_pdfs')
    timeStamp = models.DateTimeField(default=datetime.now, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.timeStamp = datetime.now()
        return super(StatisticsGallery, self).save(*args, **kwargs)

    def __str__(self):
        return self.title