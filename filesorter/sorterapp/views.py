from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UploadedFile
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
    return render(request, 'settings.html', {})
