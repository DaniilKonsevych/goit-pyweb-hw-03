# import os
# import shutil
# import concurrent.futures

# def file_handler(source, dist):
#     if not os.path.exists(source) or not os.path.isdir(source):
#         print("Folder doesn't exist.")
#         return
#     if not os.path.exists(dist) or not os.path.isdir(dist):
#         os.mkdir(dist)
#     for root, dirs, files in os.walk(source):
#         for filename in files:
#             extenstion = filename.split(".")[-1]
#             target_folder = os.path.join(destination, extenstion)
#             if not os.path.exists(target_folder):
#                 os.mkdir(target_folder)
#             file = os.path.abspath(filename)
#             shutil.copy(file, target_folder)

# if __name__ == "__main__":
#     source = r".\input"
#     destination = r".\output"
#     with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
#         results = list(executor.map(file_handler, source, destination))

import os
import shutil
import concurrent.futures


def file_handler(files, destination, root):
    for filename in files:
        extenstion = filename.split(".")[-1]
        target_folder = os.path.join(destination, extenstion)
        if not os.path.exists(target_folder):
            os.mkdir(target_folder)
        file = os.path.join(root, filename)
        file_abs = os.path.abspath(file)
        shutil.copy(file_abs, target_folder) 

def main(source, dist):
    if not os.path.exists(source) or not os.path.isdir(source):
        print("Folder doesn't exist.")
        return
    if not os.path.exists(dist) or not os.path.isdir(dist):
        os.mkdir(dist)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor: 
        for root, dirs, files in os.walk(source):
            executor.submit(file_handler, files, dist, root)
          
            

if __name__ == "__main__":
    source = r"input"
    destination = r"output"
    main(source=source, dist=destination)