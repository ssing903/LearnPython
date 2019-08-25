# Web scrapping 

# Project mapIt.py with webbrowser modules

# import webbrowser,sys

# webbrowser.open(sys.argv[1])
'''
# automate google map search 

import webbrowser,sys,pyperclip

if len(sys.argv) > 1:
     # Get the address from the command line
     address = ' '.join(sys.argv[1:])
else:
     # Get address from clipboard
     address = pyperclip.paste()
webbrowser.open('https://www.google.com/maps/place/' + address)

'''

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

