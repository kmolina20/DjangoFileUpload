from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Document(models.Model):
    title = models.CharField(max_length = 200)
    uploadedFile = models.FileField(upload_to = "uploaded_files/")
    dateTimeOfUpload = models.DateTimeField(auto_now = True)

class Query(models.Model):
    version = models.CharField(max_length = 200)
    int_exch_id = models.CharField(max_length = 200)
    int_exch_name = models.CharField(max_length = 200)