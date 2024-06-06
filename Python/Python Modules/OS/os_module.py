import os

# We can get the currect directory we are working
print(os.getcwd())

# Change the Directory we are working
os.chdir("/Users/user/OneDrive/Έγγραφα/Visual Studio 2019/Python")

# See all the files/folders in currecnt directory
# We can also put the path as a parameter
print(os.listdir())

# Create a folder in the current working directory
os.mkdir("Os Dir")

# Create folder with more folders ( We can't do that with the mkdir method )
os.makedirs("Os Dir With Dirs/ Dir-1")

# Delete folder
os.rmdir("Os Dir")

# Delete folder with folders
os.removedirs("Os Dir With Dirs/ Dir-1")

# Rename a file or a folder
try:
    os.rename("Maths", "Maths Stuffs")
    os.rename("test.txt", "Text.txt")
except:
    pass

# See information about a file 
try:
    print(os.stat("Text.txt"))
except:
    pass

#See all the files and Directory
for dir_path, dir_name, file_name in os.walk("/Users/user/OneDrive/Έγγραφα/Visual Studio 2019/Python"):
    print("Current Path: ", dir_path)
    print("Directories : ", dir_name)
    print("Files: ", file_name)
    print() 

os.chdir("/Users/jacob/Documents/USB/Programming/Python/Theory")
path = os.getcwd()
i = 0
for root, _, files in os.walk(path):
    print(root)
    for name in files:
        print(name)
    
    print()