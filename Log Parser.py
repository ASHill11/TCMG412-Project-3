# TCMG 412-501, group 0 project 2
# Server Log Parser

# READ ME
# The rough structure of the code should be as follows:
# Welcome message
# Clear cache prompt
# Ask for URL input to pull file
# (File either downloads or errors)
# Then, the program parses the data and gives what the lab asks for


# IMPORT MODULES HERE
import urllib.request
import os
import glob


# WRITE FUNCTIONS HERE
def retrieve(url):
    requested = urllib.request.urlopen(url)
    # Debug line, returns result code, comment out for final release
    print("Result: " + str(requested.getcode()))


# Welcome message
print('Howdy! Welcome to this server log parser.')
print('This program is designed to work with .txt log files from an Apache web server.')


# Default cache location
cache = r'C:\Program Files\Parser'
skip = False
# If the cache already exists in the default location it should skip this step
if not os.path.exists(cache):
    # This will skip cache clearing if used
    skip = True
    # Cache is created at the file path set in the cache variable on line 31
    os.makedirs(cache)

# This variable deals with whether a user wants to clear the cache.
# A while loop will enforce proper input
while True:
    if skip:
        break
    clear = input('Do you want to clear the cache? (y/n): ')
    if clear == 'y':
        files = glob.glob(cache)
        for f in files:
            os.remove(f)
        break
        # code to clear the cache
    elif clear == 'n':
        # If cache doesn't need to be cleared, then escape the loop
        break
    else:
        print('Invalid input detected, please try again')


UserUrl = input('Please input source URL: ')
retrieve(UserUrl)
