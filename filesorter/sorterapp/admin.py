from django.contrib import admin
from .models import UploadedFile, DocumentExtention,VideoExtention,ImageExtention,AudioExtention

# Register your models here.


admin.site.register(UploadedFile)
admin.site.register(DocumentExtention)
admin.site.register(VideoExtention)
admin.site.register(ImageExtention)
admin.site.register(AudioExtention)