from django.db import models

# Create your models here.

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
    
class DocumentExtention(models.Model):
    extention = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.extention
class ImageExtention(models.Model):
    extention = models.CharField(max_length=10, unique=True)
    def __str__(self):
        return self.extention
class AudioExtention(models.Model):
    extention = models.CharField(max_length=10, unique=True)
    def __str__(self):
        return self.extention
class VideoExtention(models.Model):
    extention = models.CharField(max_length=10, unique=True)
    def __str__(self):
        return self.extention
