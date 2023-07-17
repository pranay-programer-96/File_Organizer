import os
import shutil

#Code For File extensions and their respective folders
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Videos": [".mp4", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Spreadsheets": [".xls", ".xlsx"],
    "Presentations": [".ppt", ".pptx"],
    "Code": [".py", ".java", ".cpp"],
    "Compressed": [".zip", ".rar", ".tar.gz"],
    "Executables": [".exe", ".msi"],
    "Databases": [".sqlite", ".db"]
}

def create_folders(directory):
    # Creates folders for each file type if they don't exist
    for folder_name in FILE_TYPES.keys():
        folder_path = os.path.join(directory, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def organize_files(directory):
    create_folders(directory)

    # Scans the specified directory and move files to respective folders
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1]
            for folder_name, extensions in FILE_TYPES.items():
                if file_extension in extensions:
                    destination_folder = os.path.join(directory, folder_name)
                    shutil.move(file_path, destination_folder)
                    break

def get_directory_path():
    while True:
        directory = input("Enter the directory path to organize: ")
        if os.path.isdir(directory):
            return directory
        else:
            print("Invalid directory. Please try again.")

def print_menu():
    print("Options:")
    print("1. Organize files in a directory")
    print("2. Exit")

def file_organizer():
    while True:
        print_menu()
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            directory = get_directory_path()
            organize_files(directory)
            print("Files organized successfully!.....\n")
        elif choice == "2":
            print("Exiting file organizer...\nthank you....")
            break
        else:
            print("Invalid choice. Please try again.")

# program call
file_organizer()
