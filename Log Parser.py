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

"""
# WRITE FUNCTIONS HERE
def retrieve(url):
    requested = urllib.request.urlopen(url)
    # Debug line, returns result code, comment out for final release
    print("Result: " + str(requested.getcode()))

    Commented out for new code, outside the function its easier to take the data
"""



# Welcome message
print('Howdy! Welcome to this server log parser.')
print('This program is designed to work with .txt log files from an Apache web server.')

# Default cache location
cache = r'C:\Program Files\Parser'
skip = False
# If the cache already exists in the default location it should skip this step
if not os.path.exists(cache):
    # This will skip cache clearing if triggered
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

Text_File = urllib.request.urlopen("https%3A//s3.amazonaws.com/tcmg476/http_access_log")

Log = ""

for i in Text_File:
    Log += (str(i) + '/n')

""" 
please set the file to be a big string 
above the triple quote,
it should come that way with newline 
markers where the logs are split

just name that big string "Log" ( Log = *big string here*)
and the code below should parse the data 
and answer the questions in the lab, 
lmk if there are any issues
(432) 631 - 3606 
-Miles
"""
# to separate the file into individual logs as a list
# then take the first characters off and leave the date at the start
Log = Log.split('/n')
count = 0
for i in Log:
    spot = 0
    for j in i:
        if j == '[':
            break
        else:
            spot += 1
    i = i[spot + 4:]
    Log[count] = i
    count += 1

Total = count

count = 0

for i in Log:
    # print (i[0:3])
    # print(i[4:8])
    # right year for last 6 months?
    if i[4:8] == "1995":
        # right month?
        if i[0:3] == 'Oct':
            count += 1
        elif i[0:3] == 'Sep':
            count += 1
        elif i[0:3] == 'Aug':
            count += 1
        elif i[0:3] == 'Jul':
            count += 1
        elif i[0:3] == 'Jun':
            count += 1
        elif i[0:3] == 'May':
            count += 1
        # if not last 6 months dont count
        else:
            continue
    else:
        continue

print()
print(count, "requests have been made in the last 6 months")
print(Total, "requests are in the Log in total")
