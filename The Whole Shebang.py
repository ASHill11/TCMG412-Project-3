import urllib.request
import os
import re
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
    Log += i.decode()  # decode bytes to string

# to separate the file into individual logs as a list
# then take the first characters off and leave the date at the start
Log = Log.split('\n')
count = 0
save_path = cache
completeName = os.path.join("Cache.txt", cache)
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
        # if not last 6 months don't count
        else:
            continue
    else:
        continue


#Error requests count I dont think this is right lol
error_3_count = 0
for i in Log:
    if len(re.findall('^.*" [3][0-9]{2}', i)) > 0:
        error_3_count += 1
    else:
        continue
error_4_count = 0
for i in Log:
    if len(re.findall('^.*" [4][0-9]{2}', i)) > 0:
        error_4_count += 1
    else:
        continue


#Create an individual file for each month
jan_cache = os.path.join(cache, 'Jan')
feb_cache = os.path.join(cache, 'Feb')
mar_cache = os.path.join(cache, 'Mar')
apr_cache = os.path.join(cache, 'Apr')
may_cache = os.path.join(cache, 'May')
jun_cache = os.path.join(cache, 'Jun')
jul_cache = os.path.join(cache, 'Jul')
aug_cache = os.path.join(cache, 'Aug')
sep_cache = os.path.join(cache, 'Sep')
oct_cache = os.path.join(cache, 'Oct')
nov_cache = os.path.join(cache, 'Nov')
dec_cache = os.path.join(cache, 'Dec')


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
print("Number of error requests (4xx): ", error_4_count)
print("Number of error requests (3xx): ", error_3_count)
print(count, "requests have been made in the last 6 months")
print(Total, "requests are in the Log in total")