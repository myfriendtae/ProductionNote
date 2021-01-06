from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
import pytz

nz_tz = pytz.timezone('Pacific/Auckland')

# Create your models here.
class DayEvent(models.Model):
    create_date = models.DateTimeField(default=timezone.now)
    edit_date = models.DateTimeField(default=timezone.now)
    day_content = RichTextUploadingField(blank=True, null=True)
    # content = models.CharField(max_length=50)
    group = models.CharField(max_length=50)
    editor = models.CharField(max_length=50)
    signed_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(timezone.localtime(self.edit_date)) + '-' +  self.group +': ' +self.signed_by.username + '-' + self.editor

class NightEvent(models.Model):
    create_date = models.DateTimeField(default=timezone.now)
    edit_date = models.DateTimeField(default=timezone.now)
    night_content = RichTextUploadingField(blank=True, null=True)
    # content = models.CharField(max_length=50)
    group = models.CharField(max_length=50)
    editor = models.CharField(max_length=50)
    signed_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(timezone.localtime(self.edit_date)) + '-' +  self.group +': ' +self.signed_by.username + '-' + self.editor

class UploadFile(models.Model):
    create_date = models.DateTimeField(default=timezone.now)
    group = models.CharField(max_length=50)
    signed_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    file = models.FileField(upload_to='itn/', blank=True)

    def __str__(self):
        return str(timezone.localtime(self.edit_date)) + '-' +  self.group +': ' +self.signed_by.username