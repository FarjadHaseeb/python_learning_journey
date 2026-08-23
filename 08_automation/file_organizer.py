from pathlib import Path
import shutil

folder = Path(input("Folder to organize: ")).expanduser()

categories = {
    ".jpg": "Images", ".jpeg": "Images", ".png": "Images",
    ".pdf": "Documents", ".docx": "Documents", ".txt": "Documents",
    ".py": "Code", ".csv": "Data", ".xlsx": "Data"
}

for file in folder.iterdir():
    if file.is_file() and file.suffix.lower() in categories:
        destination = folder / categories[file.suffix.lower()]
        destination.mkdir(exist_ok=True)
        shutil.move(str(file), str(destination / file.name))

print("Organization complete.")
