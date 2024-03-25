import os
import shutil
from pathlib import Path
from .models import AudioExtention, VideoExtention, DocumentExtention, ImageExtention, UploadedFile
from zipfile import ZipFile

script_directory = Path(__file__).resolve()

def run_sorter():
    print("RUNNING SORTER")

    file_types = {
        'audios': AudioExtention.objects.values_list("extention", flat=True),
        'images': ImageExtention.objects.values_list("extention", flat=True),
        'videos': VideoExtention.objects.values_list("extention", flat=True),
        'documents': DocumentExtention.objects.values_list("extention", flat=True),
    }
    dir_parent = Path(script_directory.parent.parent)
    items_path = os.path.join(dir_parent, "media/uploads")


    for category in file_types:
        folder_path = os.path.join(items_path, category)
        os.makedirs(folder_path, exist_ok=True)

    for file_name in os.listdir(items_path):
        file_path = os.path.join(items_path, file_name)

        if os.path.isfile(file_path):
            file_type = None
            for category, extensions in file_types.items():
                if any(file_name.lower().endswith(ext) for ext in extensions):
                    file_type = category
                    break
            
            if file_type:
                print(file_type)
                destination_folder = os.path.join(items_path, file_type)
                destination_path = os.path.join(destination_folder, file_name)
                shutil.move(file_path, destination_path)
                print(f"File '{file_name}' has been moved to '{destination_path}.' ")