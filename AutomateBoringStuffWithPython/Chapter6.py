# # Manupulating Strings
# print("Hello there!\n How are you?\nI\'m doing fine.")

# Raw Strings
# print(r'Hi there\n how u doing')

# Multiline string with triple quotes
# print('''
#      How you doin'
#      I am al right
#      Are u good
# ''')

# String methods upper() lower() isUpper() isLower()
# spam = 'hello World!'.upper()
# print(spam.lower().isupper())

# print('How are you?')
# feeling = input()
# if feeling.lower() == 'great':
#      print('I feel great too')
# else:
#      print('Hope your day is goo')

# the isX String methods
# print('1.23'.isdecimal())

# while True:
#      print('Enter your age: ')
#      age = input()
#      if age.isdecimal():
#           break
#      print('Please enter a number of your age')

# while True:
#      print('Select a new password (letters and numbers only): ')
#      password = input()
#      if password.isalnum():
#           break
#      print('Enter alpha numeric password')

# The startsWith() endsWith() String methods
# print('Hello World!'.lower().startswith('hello'))
# print('Hello World!'.lower().endswith('world'))

# join() and splits() String methods
# print('-'.join(['cats','rats','bats']))

# print('My name is Khan'.upper().split('m'))

# justfiying text with rjust(), lJust() and center()
# print('Hello'.ljust(600,'*').rjust(700,'-').center(800,'='))

#picnicTable.py

# def printPicnic(itemsDict,leftWidh,rightWidth):
#      print('- PICNIC ITEMS'.center(leftWidh + rightWidth),'-')
#      for k, v in itemsDict.items():
#           print(k.ljust(leftWidh,'.') + str(v).rjust(rightWidth))

# picnicItems = {'sandwiches':4,'apples':12,'cups':4,'cookies':800}
# printPicnic(picnicItems,12,5)
# printPicnic(picnicItems,20,6)

# Removing space with strip() rStrip() lstrip()
# print(' HELLO WORLD'.strip().lstrip('H').rstrip('D').strip())

# coping and pasting string with the pyperclip module
import pyperclip

pyperclip.copy('Test')

