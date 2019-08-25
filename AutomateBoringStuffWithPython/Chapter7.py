#Pattern matching with regular expressions
# def isPhoneNumber(text):
#      if len(text) != 12:
#           return False
#      for i in range(0,3):
#           if not text[i].isdecimal():
#                return False
#      if text[3] != '-':
#           return False
#      for i in range(4,7):
#           if not text[i].isdecimal():
#                return False
#      if text[7] != '-':
#           return False
#      for i in range(8,12):
#           if not text[i].isdecimal():
#                return False
#      return True

# print('123-456-7890 is decimal: True/False : ' + str(isPhoneNumber('123-456-7890')))
# print('123-4567-890 is decimal: True/False : ' + str(isPhoneNumber('123-4567-890')))
               
# isPhoneNumber.py
# message = 'Call me at 415-515-1011 tommorrow. 415-515-1011 is my office.'
# for i in range(len(message)):
#      chunk = message[i:i+12] 
#      if isPhoneNumber(chunk):
#           print('Phone number found')
# print('Done')

# Finding patterns of text with regular expressions
# creating regex objects
import re
# print('Hello World')

# phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# Grouping with parentheses
# phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# mo = phoneNumberRegex.search('My number is 415-555-4242')
# print(mo.groups())
# print('Phone number is found ' + mo.group(1))
# print(mo.group(1))
# print(mo.group(2))

# k, x = mo.groups()
# print(k  + ' - ' + x)

# Matching multiple groups with the pipe
#hero
# heroRegex = re.compile(r'Batman|Tina Fey')
# mo  = heroRegex.search('Batman and Tina Fey . ')
# print(mo.group())
# mo = re.compile(r'Bat(man|mobile|copter|bat)').search('Batmobile lost a wheel')
# print(mo.group())

# Optional matching with the question mark

# batRegex = re.compile(r'Bat(wo)?man').search('The adventures of Batwoman and Batman')
# print(batRegex.group())

# grouping 
# hasRegex = re.compile(r'(ha){3}').search('hahaha')
# print(hasRegex.groups())

# Greedy and non-greedy matching
# greedyHaRegex = re.compile(r'(Ha){3,5}').search('HaHaHa')
# print(greedyHaRegex.group(1))

# nonGreedyRegex = re.compile(r'(Ha){3,5}?').search('HaHaHaHaHa')
# print(nonGreedyRegex.group())

# FindAll() method
# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo  = phoneNumRegex.findall('Cell: 415-555-9999 Work : 212-555-0000')
# print(mo)

# FindAll() returning list of tuples
# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') #has groups
# mo  = phoneNumRegex.findall('Cell: 415-555-9999 Work : 212-555-0000')
# print(mo)

# Character classes
# xmasRegex = re.compile(r'\d+\s\w+')
# mo = xmasRegex.findall('12 Drummers, 11 pipers, 10 lords, 9 ladies')
# print(mo)

# Making your own character classes
# vowelRegex = re.compile(r'[aeiouAEIOU]')
# mo = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
# print(mo)

#negative character classes
# consonantRegex = re.compile(r'[^aeiouAEIOU]')
# mo = consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
# print(mo)

# Ranges
# rangeRegex = re.compile(r'[a-zA-z0-9]')
# mo = rangeRegex.findall('RoboCop eats baby food. BABY FOOD.')
# print(mo)

# Caret and dollar sign character
# beginWithHello = re.compile(r'^Hello').findall('Hello')
# print(beginWithHello)

#using custom classs
# beginWithHello = re.compile(r'[^\'Hello\']').findall('Hello World')
# print(beginWithHello)

# beginWithHello = re.compile(r'^Hello').search('hello World!')
# print(beginWithHello == None)

# endsWithNumber = re.compile(r'^\d+$').search('1234567890')
# print(endsWithNumber.group())

# the wildcard character 
# atRegex = re.compile(r'.').findall('The cat in the hat sat on flat mat.')
# print(atRegex)

# Watching everything with dot star
# nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)').search('First Name: Al Last Name: Sweigart')
# print(nameRegex.groups())

# nonGreedyRegex = re.compile(r'<.*?>').search('<To serve man> for dinner.>')
# print(nonGreedyRegex.group())

# Greedy Regex
# greedyRegex = re.compile(r'<.*>').search('<To serve man> for dinner.>')
# print(greedyRegex.group())

# Matching new line with the dot character
# noNewLineRegex = re.compile('.*',re.DOTALL).search('Serve the public trust.\nProtect the innocent.\nUphold the law')
# print(noNewLineRegex.group())

# Case- insensitive matching
# regex1 = re.compile(r'RoboCop',re.I).search('ROBOCOP is part man, part machine, all cop.').group()
# print(regex1)

# Subsituting Strings with sub() methods
# nameRegex = re.compile(r'Agent \w+').sub('CENSORED','Agent Alice gave the secret documents to Agent Bob.')
# print(nameRegex)

# agentNameRegex = re.compile(r'Agent (\w)\w*').sub(r'\1****','Agent Alice told Agent Carol')
# print(agentNameRegex)

# Managing complex regexes
# Phone number and email address extractor
# phoneAndEmail.py

