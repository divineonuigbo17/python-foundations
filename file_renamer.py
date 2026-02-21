import os

# Path to the folder with files to rename
folder_path = "test_files"

# Make sure the folder exists
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f"Created folder '{folder_path}'. Add some files to rename.")
else:
    files = os.listdir(folder_path)

    for index, filename in enumerate(files, start=1):
        # Split name and extension
        name, ext = os.path.splitext(filename)
        new_name = f"file_{index}{ext}"
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed '{filename}' to '{new_name}'")