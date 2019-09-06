'''
This program looks in a specified directory and finds all files with a certain extension. It finds and replaces the specified words.
Developed by: Sage Hourihan
Date: 7/2/19
'''
# importing modules
import os # This module provides a portable way of using operating system dependent functionality.
import sys # This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available.
import fileinput # This module implements a helper class and functions to quickly write a loop over standard input or a list of files. 
import glob # The glob module finds all the pathnames matching a specified pattern according to the rules used by the Unix shell, although results are returned in arbitrary order. No tilde expansion is done, but *, ?, and character ranges expressed with [] will be correctly matched. 
import time # This module provides various time-related functions. For related functionality, see also the datetime and calendar modules.

def textreplace():
    
    # creating instructions and variables
    print ("File directory path: ")
    path = input(r"> ")
    print ("Extension you are looking for (include period): ")
    ext = input(r"> ")
    print ("Text to search for:")
    textToSearch = input(r"> ") 
    print ("Text to replace it with:")
    textToReplace = input(r"> ")
    # combining path with backslash, wildcard, and extension
    f = path+'\*'+ext

    # starting timer
    start_time = time.time()

    # creating function
    def fndRplc():
    # for loop that loops through all specific files in directory
        for fname in glob.glob(f):
    # opening files with read and write permissions
            tempFile = open( fname, 'r+' )
    # for loop to search for word specified
            for line in fileinput.input( fname ):
    # if statement to see if word is found in file
                if textToSearch in line :
                    print('Match Found') # output
                else:
                    print('Match Not Found!!') # output
    # writing to files and replacing the specific words
                tempFile.write( line.replace( textToSearch, textToReplace ) ) 
    # closing file
            tempFile.close() 

    # calling function, timer stop
    fndRplc()
    elapsed_time = round(time.time() - start_time)

    print('It took: ',elapsed_time, ' seconds to run.') # output
    input( '\t Press Enter to exit...' ) #exit
