import os

folders = input("Please provide list of folder names with spaces in between: ")

# Convert the provided string to a list => will use split function
folders_list= folders.split()

# iterate over folders_list to print the files of each folders
# will make use of os method to list all the files of that particular folder
for folder in folders_list:
    

    try:
       files= os.listdir(folder)
    except FileNotFoundError:
        print("Please provide a valid folder name, looks like folder doesn't exist:"+ folder)
        continue
    except PermissionError:
        print("No access to this file")
        continue

    print("*****Listing files of the folder*****: " + folder)

    for file in files:
        print(file)


