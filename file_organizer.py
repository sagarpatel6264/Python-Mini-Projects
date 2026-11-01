import os
import shutil

def organize_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.log'):
            if not os.path.exists('logs'):
                os.makedirs('logs')
            shutil.move(filename, 'logs/' + filename)
            print(f"Moved {filename} to logs folder")

# organize_files('./server_data')
