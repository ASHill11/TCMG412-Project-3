# TCMG 412-501, group 0 project 2
# Server Log Parser

# READ ME
# The rough structure of the code should be as follows:
# Welcome message
# Clear cache prompt
# Ask for URL input to pull file
# (File either downloads or errors)
# Then, the program parses the data and gives what the lab asks for


# Welcome message
print('Howdy! Welcome to this server log parser.')
print('This program is designed to work with .txt log files from an Apache web server.')
print()

# this variable deals with whether a user wants to clear the cache. A response of yes will set it to 1
# A response of no will set it to 0
# A while loop will enforce proper input
while True:
    clear = input('Do you want to clear the cache? (y/n): ')
    if clear.isalpha():
        if clear == 'y' or 'Y':
            break
            # code to clear the cache
        elif clear == 'n' or 'N':
            # If cache doesn't need to be cleared, then escape the loop
            break
        else:
            print('Invalid input detected, please try again')
    else:
        print('Invalid input detected, please try again')
