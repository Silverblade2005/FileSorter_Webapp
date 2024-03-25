from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UploadedFile, AudioExtention, VideoExtention,DocumentExtention,ImageExtention
from .sorter_module import run_sorter
import os

# Create your views here.

def home(request):
    if request.method == "POST":
        files = request.FILES.getlist("files_to_sort") 

        for file in files:
            new_file = UploadedFile(file=file)
            new_file.save()

        zip_file = run_sorter()

        print(f"Zip File {zip_file}")

        with open(zip_file, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/zip')

            response['Content-Type'] = 'application/zip'

            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(zip_file)}"'


            return response

        
    return render(request, 'index.html', {})

def settings(request):

    if request.method == "POST":
        is_video = request.POST.get('is_video')
        is_audio = request.POST.get('is_audio')
        is_document = request.POST.get('is_document')
        is_image = request.POST.get('is_image')
        extention_field = request.POST["extention_field"]

        if is_video != None:
            new_ext = VideoExtention(extention=extention_field)
            new_ext.save()
        if is_audio != None:
            new_ext = AudioExtention(extention=extention_field)
            new_ext.save()
        if is_document != None:
            new_ext = DocumentExtention(extention=extention_field)
            new_ext.save()
        if is_image != None:
            new_ext = ImageExtention(extention=extention_field)
            new_ext.save()
        
        

    return render(request, 'settings.html', {
        "AudioExtentions": AudioExtention.objects.all(),
        "VideosExtentions": VideoExtention.objects.all(),
        "ImagesExtentions": ImageExtention.objects.all(),
        "DocumentExtentions": DocumentExtention.objects.all(),
    })
