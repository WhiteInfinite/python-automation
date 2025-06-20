from pathlib import Path

filenames = input("Enter filenames separated by commas: ").split(",")
filenames = [s.lstrip() for s in filenames]

for name in filenames:
    file = Path(name)
    folder = Path(file.stem)
    folder.mkdir(exist_ok=True)
    print(f"Folder '{folder}' created")
    if file.exists() and file.is_file():
        new_path = folder / file.name
        file.rename(new_path)
        print(f"Moved {file} to the Folder {folder}")


'''Creates folder for each file and moves the file into the folder, if file exists.'''
