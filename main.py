import os
import sys

#####
# Recursive File lister.
# Receives one argument which is the folder to list the content of
# Made By : Mor Yosef
# 21-Jan-21
#####

# for the sake of testing i found setting an alias to 'python main.py' very effective


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


#  an empty list which will be populated with the data we need to write to the file
csv_data = []



# receives one parameter which is the path to proceed on
def rec_lister(target_path):
  if( os.path.isdir(target_path)):
    print("Tomatoe sauce")




#Reading the target folder from the arguments
target_folder = ' '.join(sys.argv[1:]) #using a ' '.join we make sure to grab a whole folder name or path even if the user forgot to use quotes

if not os.path.isdir(target_folder): #testing to see if received argument is in fact a dir.
  print("Specified argument is not an existing folder") # if its not , print it out to the user
  exit() # And exit the program!

# since we know for sure we have a green light to start, we are going to create a csv file.
csv_file = open("rec_csv.csv", 'w')



if __name__ == "__main__":
  rec_lister(target_folder)  
 
  csv_file.writelines(csv_data)
  csv_file.close()
  print("Procedure finished")
