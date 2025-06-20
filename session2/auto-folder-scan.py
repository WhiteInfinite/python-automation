from pathlib import Path
import os

folder = input("Enter folder name: ")
folder_path = Path(folder)

for item in folder_path.iterdir():
    if item.is_file():
        suffix = item.suffix.lstrip('.')
        if not suffix:
            continue 
        target_folder = folder_path / suffix
        target_path = target_folder / item.name
        if not target_folder.exists():
            os.makedirs(target_folder)

        try:
            os.rename(item, target_path)
            print(f"Moved: {item.name} into Folder: {target_folder.name}")
        except Exception as e:
            print(f"Error moving {item.name}: {e}")

