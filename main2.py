import os
import sys
#Changing usage from checksumdir.dirhash to dirhashdirhash
#from checksumdir import dirhash #for directory hash

from dirhash import dirhash
import hashlib # for file hash

# for debug
from datetime import datetime



#####
# Recursive File lister.
# Receives one argument which is the folder to list the content of
# Made By : Mor Yosef
# 21-Jan-21
#####

# for the sake of testing i found setting an alias to 'python main.py' very effective
#adding a comment to test

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


# canceled the "csv_data" and the append and the 'write lines' going to write independant lines at a time
#  an empty list which will be populated with the data we need to write to the file
csv_data = []
current_data_entry = 0


def my_get_md5hash(object_path):
  try: # it checks to see if the target is a dir or a file
    if (os.path.isdir(object_path) == True):
      # as nice as it was, it gave me trouble on some folders like /proc/1/cwd/proc/1/cwd/dev
      #return dirhash(object_path , 'md5') #returns a directory md5 # switched to using a different one
      #returned to using the popen i used for files for the directories since the dirhashes get stuck on some special folders
      popen_stdin,popen_stdout,popen_stderr= os.popen3('timeout 12s tar -cf - "'+object_path+'" | md5sum')
      popen_stdout = popen_stdout.read().split(" ")[0]
      popen_stderr = popen_stderr.read()
      if popen_stderr.__contains__("denied") :
        return "Premission denied"
      elif popen_stderr.__contains__("changed as we read it"):
        return "changed while was read"
      else:
        return popen_stdout
    elif os.path.islink(object_path): # unfortunately i had to catch link because of the program jamming on /proc//1/cwd/proc , read online a way to avoid these is to avoid links
      return "Is a link" 
    else:
      return hashlib.md5(object_path).hexdigest() #returns a file md5
  except:
    return( "Skipped due to error") #since it sometimes errors i want it to try catch.
      

# a function that receives a path , and lists everything under it recursively
def rec_lister(target_path):
  #not the most efficient, but brought mt trouble
  target_path = target_path.replace('//','/')
  # reading the ls results
  ls_results = os.popen( 'ls "{}"'.format(target_path))
  # converting the bulk 'file' to a list of entries
  ls_results = ls_results.readlines()
  for i in ls_results:
    global current_data_entry
    current_data_entry += 1
    csv_data.append("")
    if target_path != '/':
      object_path = target_path+"/"+i[:-1]
    else:
      object_path = "/" + i[:-1]
    print(str(current_data_entry)+"     "+object_path+"    "+str(datetime.now()) )
    md5hash = my_get_md5hash(object_path)  
    

    # changing the way im working ,going to use 'write line' instead of writing a large number of lines
    #csv_data.append(current_data_entry+", "+object_path+" , "+md5hash+"\n")
    #switched to writing to a line instead of working on a list which (After checking 'ls -R var |wc -l' figured out some of these will contain more then 30k-40k list entries
    csv_file.write(str(current_data_entry)+", "+object_path+" , "+md5hash+"\n")
    if( os.path.isdir(object_path) and not os.path.islink(object_path)):
      rec_lister(object_path)



#Reading the target folder from the arguments
target_folder = ' '.join(sys.argv[1:]) #using a ' '.join we make sure to grab a whole folder name or path even if the user forgot to use quotes

if not os.path.isdir(target_folder): #testing to see if received argument is in fact a dir.
  print("Specified argument is not an existing folder") # if its not , print it out to the user
  exit() # And exit the program!


# since we know for sure we have a green light to start, we are going to create a csv file.
csv_file = open("rec_csv2.csv", 'w').close() # EMPTIES THE FILE
csv_file = open("rec_csv2.csv", 'a') #starts writing into it (with append)

while target_folder.__contains__('//'):
  target_folder = target_folder.replace('//','/')

if __name__ == "__main__":
  rec_lister(target_folder)  
  # going to change the way the program works , im going to writeline instead of lines for each csv entry
  csv_file.close()
  print("Done...")
