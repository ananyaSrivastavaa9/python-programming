# Importing the os module to interact with operating system
import os

# Set directory to current folder
directory = "."

# Get list of all files and folders in the directory
files = os.listdir(directory)

# Print the list of files and folders
print(files)
