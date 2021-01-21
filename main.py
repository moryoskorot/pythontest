# python exam 
import os
import sys
#####
# Recursive File lister.
# Receives one argument which is the folder to list the content of
# Made By : Mor Yosef
# 21-Jan-21
#####

# Get the current working directory: os.getcwd()
# Change the current working directory: os.chdir()
# sys.argv[1] (to handle  arguments)
#
#  data = ' '.join(sys.argv[1:]) 

target_folder = sys.argv[1]

stream = os.popen('echo Returned output')
output = stream.read()  
