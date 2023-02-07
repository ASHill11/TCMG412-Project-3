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
    # Variable for skipping cache clearing if this block is used
    # Not used in this block
    skip = True
    # Prompt the user if they want a custom cache, will use preset if not.
    # Can't currently think of a way to avoid this prompt if the user previously entered a custom cache
    while True:
        custom = str(input('Do you wish to set a custom cache location? (Not recommended)(y/n): '))
        if custom.isalpha():
            if custom[0] == 'y' or 'Y':
                location = input('Enter file path of desired directory: ')
                customlocation = location + 'Parser'
                # customlocation2 =
                # DEBUG LINE, comment out for release
                print(customlocation)
                try:
                    os.makedirs(customlocation)
                except:
                    print('Error creating cache')
                else:
                    print('Success! Cache is named \"Parser\"')
                    break
            elif custom[0] == 'n' or 'N':
                os.makedirs(cache)
                break
            else:
                print('Invalid input detected, please try again')
        else:
            print('Invalid input detected, please try again')

# This variable deals with whether a user wants to clear the cache.
# A while loop will enforce proper input
while True:
    if skip:
        break
    clear = input('Do you want to clear the cache? (y/n): ')
    if clear == 'y' or 'Y':
        break
        # code to clear the cache
    elif clear == 'n' or 'N':
        # If cache doesn't need to be cleared, then escape the loop
        break
    else:
        print('Invalid input detected, please try again')


UserUrl = input('Please input source URL: ')
retrieve(UserUrl)
