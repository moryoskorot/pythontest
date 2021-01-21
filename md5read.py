import os

#small debugging program to see how can i get popen to not spit output on stdout
#my problem was that the popen gave err output to the screen, which i disaproove :(


testing = os.popen('md5sum main.py').read()
print(testing.split(" ")[0] + " is the hash of main.py")
testing = os.popen3('md5sum dir1')
#print(testing[0].read())
print('')
print(testing[1].read())
print('')
print(testing[2].read())
