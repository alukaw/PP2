import os

file_path = r"file_to_delete.txt"

if os.path.exists(file_path):
    if os.access(file_path, os.W_OK):
        os.remove(file_path)
        print(f"Deleted: {file_path}")
    else:
        print("No write access to delete the file.")
else:
    print("File does not exist.")
