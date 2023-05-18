import os

def check_file(name):
    path = f"./{name}"
    file_present = os.path.exists(path)
    print(check_file)
    return file_present