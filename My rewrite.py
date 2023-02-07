import urllib.request
import os
import glob


#welcome message
print('Howdy! Welcome to this server log parser.')
print('This program is designed to work with .txt log files from an Apache web server.')
url = input('Input your URL here: ')
#inputs url and gives status
rec_url = urllib.request.urlopen(url)
print("Response Status: "+ str(rec_url.getcode()))
#Save data in url as text file

#divide text by line
