#!/bin/python2.7
import os
import sys

from dirhash import dirhash
import hashlib # for file hash

#####
# Recursive File lister.
# Receives one argument which is the folder to list the content of
# Made By : Mor Yosef
# 21-Jan-21
#####

# a variable used to keep an index of the csv
current_data_entry = 0

def my_get_md5hash(object_path):
  try: # it checks to see if the target is a dir or a file
    if (os.path.isdir(object_path) == True):
      # back  to using the popen instead of the external dirhash due to issues
      popen_stdin,popen_stdout,popen_stderr= os.popen3('timeout 12s tar -cf - "'+object_path+'" | md5sum')
      popen_stdout = popen_stdout.read().split(" ")[0]
      popen_stderr = popen_stderr.read()
      if popen_stderr.__contains__("denied") :
        return "Premission denied"
      elif popen_stderr.__contains__("changed"):
        return "changed while was read"
      else:
        return popen_stdout
    elif os.path.islink(object_path): # unfortunately i had to catch link because of the program jamming on /proc//1/cwd/proc , read online a way to avoid these is to avoid links and since a link points to a file/dir that exists elsewhere, it will get mapped if you try to map that specific area
      return "Is a link" 
    else:
      return hashlib.md5(object_path).hexdigest() #returns a file md5
  except:
    return( "Skipped due to error") #since it sometimes errors i want it to try catch.
      

# a function that receives a path , and lists everything under it recursively
def rec_lister(target_path):
  # Noticed that sometimes i get double slashes, since it is ignored, decided to remove them to be cleaner
  target_path = target_path.replace('//','/')
  # reading the ls results, used popen3 to eliminate stderr mess on screen
  ls_stdin,ls_results,ls_stderr = os.popen3( 'ls "{}"'.format(target_path))
  # converting the bulk 'file' to a list of entries
  ls_results = ls_results.readlines()
  for i in ls_results:
    # Letting the program know i am reffering to the global "currnet_data_entry"
    global current_data_entry
    current_data_entry += 1
    if target_path != '/':
      object_path = target_path+"/"+i[:-1]
    else:
      object_path = "/" + i[:-1]
    md5hash = my_get_md5hash(object_path)  
    
    # on earlier versions i used to build a large list and then attempt to push it at once, but it leads to problem when it gets really large (on a small vm)
    csv_file.write(str(current_data_entry)+", "+object_path+" , "+md5hash+"\n")
    #if the item i just logged into the csv, is a directory (and not a link to one) ->proceed
    if( os.path.isdir(object_path) and not os.path.islink(object_path)):
      rec_lister(object_path)



#Reading the target folder from the arguments
target_folder = ' '.join(sys.argv[1:]) #we make sure to grab a whole folder name or path even if the user forgot to use quotes 

if not os.path.isdir(target_folder): #testing to see if received argument is in fact a dir.
  print("Specified argument is not an existing folder") # if its not , print it out to the user
  exit() # And exit the program!


# since we know for sure we have a green light to start, we are going to create a csv file.
csv_file = open("rec_csv2.csv", 'w').close() # FLISHINGA THE TARGET FILE
csv_file = open("rec_csv2.csv", 'a') #starts writing into it (with append)

while target_folder.__contains__('//'): # to avoid things like ///home//////root or anything like that
  target_folder = target_folder.replace('//','/')

if __name__ == "__main__":
  print("This might take a while depending on your target...")
  rec_lister(target_folder)  
  # going to change the way the program works , im going to writeline instead of lines for each csv entry
  csv_file.close()
  print("Done...")
