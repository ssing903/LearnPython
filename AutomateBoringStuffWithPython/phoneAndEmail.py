#! python3
# phoneAndEmail.py - Finds phone numbers and email address on the clipboards

import pyperclip,re

phoneRegex = re.compile(r'''(
     (\d{3}|\(\d{3}\))?  # Area code
     (\s|-|\.)?     # Seperator
     (\d{3})        # First 3 digits
     (\s|-|\.)      # seprator
     (\d{4})        # last 4 digits
     (\s*(ext|x|ext.)\s*(\d{2,5}))?     # extension
     )''',re.VERBOSE)

# create email regex.
emailRegex = re.compile(r'''(
     [a-zA-Z-0-9._%+-]+  #username
     @                   # @symbol
     [a-zA-Z0-9.-]+      # domain name
     (\.[a-zA-Z]{2,4})   # dot something
     )''',re.VERBOSE)

# find matches in clipboard text
text  = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
     phoneNum = '-'.join([groups[1],groups[3],groups[5]])
     if groups[8] != '':
          phoneNum += ' x' + groups[8]
     matches.append(phoneNum)
for groups in emailRegex.findall(text):
     matches.append(groups[0])
# find results to the clipboard
if len(matches) > 0:
     pyperclip.copy('\n'.join(matches))
     print('Copied to clipboard')
     print('\n'.join(matches))
else:
     print('No phone numbers or email address found')