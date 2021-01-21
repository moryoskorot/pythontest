import os
import sys

#####
# Recursive File lister.
# Receives one argument which is the folder to list the content of
# Made By : Mor Yosef
# 21-Jan-21
#####


# some functions  i grabbed from the internet
#
# os.system(command) outputs it right away
# varaible = os.popen(command) redirects the output
# variable.read() gives the bulk of the data
# variable.readline() reads a single line

# Get the current working directory: os.getcwd()
# Change the current working directory: os.chdir()
# is something a directory [-d FOLDER]
# sys.argv[1] (to handle  arguments)
#  data = ' '.join(sys.argv[1:]) # if the user wants spaced names and forgets quotes
# os.path.isdir('name') checks to see if something is a directory


#Reading and printing the
target_folder = ' '.join(sys.argv[1:])
print(os.path.isdir(target_folder))







