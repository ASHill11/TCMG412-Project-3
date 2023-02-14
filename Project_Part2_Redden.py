# TCMG 412-501, group 0 project 3
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
# import glob

# Welcome message
print('Howdy! Welcome to this server log parser.')
print('This program will cache and parse a provided server log.')
print('Please ensure that that this program is run in administrator mode')
print('NOTICE: This may take several minutes')

# Default cache location
cache = r'C:\Program Files\Parser'
# If the cache already exists in the default location it should skip this step
if not os.path.exists(cache):
    # This will skip cache clearing if triggered
    skip = True
    # Cache is created at the file path set in the cache variable on line 31
    os.makedirs(cache)

# This variable deals with whether a user wants to clear the cache.
# A while loop will enforce proper input

Text_File = urllib.request.urlopen("http://s3.amazonaws.com/tcmg476/http_access_log")
Log = ""

for i in Text_File:
    Log += (str(i) + '/n')



# to separate the file into individual logs as a list
# then take the first characters off and leave the date at the start
Log = Log.split('/n')
count = 0
save_path = cache
completeName = os.path.join(cache, "Cache.txt")
file1 = open(completeName, "w")
for i in Log:
    file1.write(i)
    spot = 0
    for j in i:
        if j == '[':
            break
        else:
            spot += 1
    i = i[spot + 4:]
    Log[count] = i
    count += 1

file1.close()
Total = count

jan_cache = r'C:\Program Files\Parser'
feb_cache = r'C:\Program Files\Parser'
mar_cache = r'C:\Program Files\Parser'
apr_cache = r'C:\Program Files\Parser'
may_cache = r'C:\Program Files\Parser'
jun_cache = r'C:\Program Files\Parser'
jul_cache = r'C:\Program Files\Parser'
aug_cache = r'C:\Program Files\Parser'
sep_cache = r'C:\Program Files\Parser'
oct_cache = r'C:\Program Files\Parser'
nov_cache = r'C:\Program Files\Parser'
dec_cache = r'C:\Program Files\Parser'


for i in Log:
    # print (i[0:3])
    # print(i[4:8])
    # right year for last 6 months?
    if i[0:3] == 'Jan':
        if not os.path.exists(jan_cache):
            # This will skip cache clearing if triggered
            skip = True
            # Cache is created at the file path set in the cache variable on line 31
            os.makedirs(jan_cache)
            save_path = cache
            completeName = os.path.join(cache, "Cache.txt")
            file1 = open(completeName, "w")
    if i[0:3] == 'Feb':
        if not os.path.exists(feb_cache):
            # This will skip cache clearing if triggered
            skip = True
            # Cache is created at the file path set in the cache variable on line 31
            os.makedirs(feb_cache)
            save_path = cache
            completeName = os.path.join(cache, "Cache.txt")
            file1 = open(completeName, "w")
    if i[0:3] == 'Mar':
        if not os.path.exists(mar_cache):
            # This will skip cache clearing if triggered
            skip = True
            # Cache is created at the file path set in the cache variable on line 31
            os.makedirs(mar_cache)
            save_path = cache
            completeName = os.path.join(cache, "Cache.txt")
            file1 = open(completeName, "w")
        # if not last 6 months don't count
    if i[0:3] == 'Apr':
        if not os.path.exists(apr_cache):
            # This will skip cache clearing if triggered
            skip = True
            # Cache is created at the file path set in the cache variable on line 31
            os.makedirs(apr_cache)
            save_path = cache
            completeName = os.path.join(cache, "Cache.txt")
            file1 = open(completeName, "w")
        # if not last 6 months don't count
    if i[0:3] == 'May':
        if not os.path.exists(may_cache):
            # This will skip cache clearing if triggered
            skip = True
            # Cache is created at the file path set in the cache variable on line 31
            os.makedirs(may_cache)
            save_path = cache
            completeName = os.path.join(cache, "Cache.txt")
            file1 = open(completeName, "w")
        # if not last 6 months don't count
    if i[0:3] == 'Jun':
        if not os.path.exists(jun_cache):
            # This will skip cache clearing if triggered
            skip = True
            # Cache is created at the file path set in the cache variable on line 31
            os.makedirs(jun_cache)
            save_path = cache
            completeName = os.path.join(cache, "Cache.txt")
            file1 = open(completeName, "w")
    if i[0:3] == 'Jul':
        if not os.path.exists(jul_cache):
            # This will skip cache clearing if triggered
            skip = True
            # Cache is created at the file path set in the cache variable on line 31
            os.makedirs(jul_cache)
            save_path = cache
            completeName = os.path.join(cache, "Cache.txt")
            file1 = open(completeName, "w")
    if i[0:3] == 'Aug':
        if not os.path.exists(aug_cache):
            # This will skip cache clearing if triggered
            skip = True
            # Cache is created at the file path set in the cache variable on line 31
            os.makedirs(aug_cache)
            save_path = cache
            completeName = os.path.join(cache, "Cache.txt")
            file1 = open(completeName, "w")
    if i[0:3] == 'Sep':
        if not os.path.exists(sep_cache):
            # This will skip cache clearing if triggered
            skip = True
            # Cache is created at the file path set in the cache variable on line 31
            os.makedirs(sep_cache)
            save_path = cache
            completeName = os.path.join(cache, "Cache.txt")
            file1 = open(completeName, "w")
    if i[0:3] == 'Oct':
        if not os.path.exists(oct_cache):
            # This will skip cache clearing if triggered
            skip = True
            # Cache is created at the file path set in the cache variable on line 31
            os.makedirs(oct_cache)
            save_path = cache
            completeName = os.path.join(cache, "Cache.txt")
            file1 = open(completeName, "w")
    if i[0:3] == 'Nov':
        if not os.path.exists(nov_cache):
            # This will skip cache clearing if triggered
            skip = True
            # Cache is created at the file path set in the cache variable on line 31
            os.makedirs(nov_cache)
            save_path = cache
            completeName = os.path.join(cache, "Cache.txt")
            file1 = open(completeName, "w")
    if i[0:3] == 'Dec':
        if not os.path.exists(dec_cache):
            # This will skip cache clearing if triggered
            skip = True
            # Cache is created at the file path set in the cache variable on line 31
            os.makedirs(dec_cache)
            save_path = cache
            completeName = os.path.join(cache, "Cache.txt")
            file1 = open(completeName, "w")
        else:
            continue
    else:
        continue

print()
print(count, "requests have been made in the last 6 months")
print(Total, "requests are in the Log in total")