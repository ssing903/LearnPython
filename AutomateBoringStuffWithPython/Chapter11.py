# Web scrapping 

# Project mapIt.py with webbrowser modules

# import webbrowser,sys

# webbrowser.open(sys.argv[1])

# automate google map search 

# import webbrowser,sys,pyperclip

#if len(sys.argv) > 1:
     # Get the address from the command line
     #address = ' '.join(sys.argv[1:])
#else:
     # Get address from clipboard
     #address = pyperclip.paste()
     #print('Hello World')
#webbrowser.open('https://www.google.com/maps/place/' + address)
# webbrowser.open(sys.argv[1])



# Downloading files from the web with requests Modules

'''
import requests

res = requests.get('https://automatetheboringstuff.com/files/pagedoesnt')
# print(type(res))
res.raise_for_status

# res.status_code == requests.codes.ok
# print(requests.codes.ok)
print(res.text)

# Checking for errors
'''

# Saving downloaded files to hard drive

'''
import requests,os

os.chdir('C:\\Users\Sukh\Desktop')
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.raise_for_status())
playFile = open('RomeoAndJuliet.txt','wb')
for chunk in res.iter_content(1000):
     playFile.write(chunk)
playFile.close()
'''

# HTML 
'''
import os, requests,bs4

os.chdir('C:\\Users\Sukh\Desktop')
exampleFile = open('example.html')
for i in exampleFile:
     print(i)
# print(exampleFile)
'''

# Finding an element with select() method
'''
import requests, bs4
res = requests.get('https://igma.im')
res.raise_for_status()
print(bs4.BeautifulSoup(res.text))
'''

'''
import os,bs4
os.chdir('C:\\Users\Sukh\Desktop')


exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile,features="html.parser")

# list = exampleSoup.select('#author')
# for i in list:
#      # print(i.getText())
#      print(i.attrs.values())

# getting data from element's attributes
spanElem = exampleSoup.select('span')
print(spanElem)

'''

# I am feeling lucky google project
# This one is nice

'''
1. Gets search keywords from command line arguments
2. Retrive the serach results page
3. Open a browser tab for each result
'''

# lucky.py

