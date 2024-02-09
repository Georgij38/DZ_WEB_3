import os
from concurrent.futures import ThreadPoolExecutor
import sys

dict_file_paths = {'audio': [], 'video': [], 'images': [], 'documents': [], 'archives': [], 'unknown': []}
file_types = {
    "images": ["jpeg", "png", "jpg", "svg", "bmp"],
    "video": ["avi", "mp4", "mov", "mkv"],
    "documents": ["doc", "docx", "txt", "pdf", "xls", "xlsx", "pptx"],
    "audio": ["mp3", "ogg", "wav", "amr", "mpeg", "aiff", "aif", "tak"],
    "archives": ["zip", "gz", "tar", "rar"],
}

def list_files_folder(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                sort_file(file_path)

def sort_file(file_path):
    file_name = os.path.basename(file_path)
    for file_type, extensions in file_types.items():
        if file_name.lower().endswith(tuple(extensions)):
            dict_file_paths[file_type].append(file_path)
            break
    else:
        dict_file_paths['unknown'].append(file_path)

def move_file(file_path, folder):
    try:
        file_name = os.path.basename(file_path)
        os.rename(file_path, os.path.join(folder, file_name))
    except Exception as e:
        print(f"Error moving file {file_path}: {e}")

def creating_folder(path, name_folder):
    new_path_folder = os.path.join(path, name_folder)
    if not os.path.exists(new_path_folder):
        os.mkdir(new_path_folder)
    return new_path_folder

def move_files_thread(file_list, folder):
    for file_path in file_list:
        move_file(file_path, folder)

def start_sort_file_exit():
    path = input('Enter the full path to the folder: ')
    if path.lower() == 'exit':
        exit()
    else:
        this_is_folder(path)

def this_is_folder(path):
    if os.path.exists(path):
        sorting_files(path)
    else:
        print ('No such folder exists')
        start_sort_file_exit()

def sorting_files(directory):
    list_files_folder(directory)
    with ThreadPoolExecutor(max_workers=4) as executor:
        for file_type, file_list in dict_file_paths.items():
            if len(file_list) != 0:
                p_dirs = creating_folder(directory, file_type)
                executor.submit(move_files_thread, file_list, p_dirs)

def main():
    if len(sys.argv) == 2:
        path = sys.argv[1]
        this_is_folder(path)
        print(path)
    else:
        start_sort_file_exit()

if __name__ == "__main__":

    main()

