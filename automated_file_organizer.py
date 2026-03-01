import os
import shutil

# Change this to the folder you want to organize
source_folder = "C:/Users/YourName/Downloads"

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Spreadsheets": [".xlsx", ".csv"],
    "Videos": [".mp4", ".mkv"],
    "Programs": [".exe", ".msi"]
}

for folder in file_types:
    folder_path = os.path.join(source_folder, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)

    if os.path.isfile(file_path):
        for folder, extensions in file_types.items():
            if any(file.endswith(ext) for ext in extensions):
                shutil.move(file_path, os.path.join(source_folder, folder, file))
                break

print("Files organized successfully.")
