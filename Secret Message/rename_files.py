import os

def rename_files():
    #(1) Get file names from folder
    file_list = os.listdir("./prank/")
    print(file_list)
    saved_path = os.getcwd()
    os.chdir("./prank/")

    #(2) For each file, rename it
    for file_name in file_list:
        print("Old name - " + file_name)
        print("New name - " + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)

rename_files()
