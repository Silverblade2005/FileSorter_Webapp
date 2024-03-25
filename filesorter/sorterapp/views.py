from django.shortcuts import render
from .models import UploadedFile
from .sorter_module import run_sorter

# Create your views here.

def home(request):
    if request.method == "POST":
        files = request.FILES.getlist("files_to_sort") 

        for file in files:
            new_file = UploadedFile(file=file)
            new_file.save()

        run_sorter()

        
    return render(request, 'index.html', {})

def settings(request):
    return render(request, 'settings.html', {})
