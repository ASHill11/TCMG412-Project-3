import urllib.request
import os
import glob




# Separate cache creation
# Default cache location
cache = r'C:\Program Files'
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

#welcome message
print('Howdy! Welcome to this server log parser.')
print('This program is designed to work with .txt log files from an Apache web server.')
url = input('Input your URL here: ')



#inputs url and gives status
def retrieve(url):
    global rec_url
    rec_url = urllib.request.urlopen(url)
    print("Response Status: "+ str(rec_url.getcode()))
    return rec_url
#Save data in url as text file

retrieve(url)
print(rec_url)


#divide text by line
