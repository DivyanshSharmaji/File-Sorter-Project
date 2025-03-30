import os
import shutil

def create_subfolder(folder_path, subfolder_name):
    subfolder_path = os.path.join(folder_path, subfolder_name)
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)

    return subfolder_path

def clean_folder(folder_path):
    # You can learn about these methods from the respective library documentations.
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path,filename)
        if os.path.isfile(file_path):
            # print(f"{file_path}\n") # For checking if the file_path is retrieved correctly or not
            file_extension = filename.split('.')[-1].lower()
            if file_extension:
                subfolder_name = f"{file_extension.upper()} Files"
                subfolder_path = create_subfolder(folder_path,subfolder_name)
                new_location = os.path.join(subfolder_path,filename)
                if not os.path.exists(new_location):
                    shutil.move(file_path, subfolder_path) 
                    print(f"Moved: {filename} --> {subfolder_name}/")
                else:
                    print(f"Skipped: {filename} already exists in {subfolder_name}/")


if __name__ =="__main__":
    print("Desktop Cleaner Script")
    folder_path = input("Enter the folder path which you want to clean: ")

    # You can find the path from cmd, by opening the cmd in the desired folder and type cd and copy the path shown.

    if os.path.isdir(folder_path):
        clean_folder(folder_path)
        print("Cleaning complete")
    else:
        print("Invalid folder path. Please ensure that the path is correct and try again.")