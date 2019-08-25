# Reading and writing files

# import os
# path = os.path.join('user','bin','spam')
# print(path)
# myFiles = ['account.txt','details.csv','invite.docx']
# for filename in myFiles:
#      print(os.path.join('C:\\Users\\sukh\\Desktop'),filename)

# Current working directory

# import os
# print(os.getcwd())
# os.chdir('C:\\Users\\sukh\\Desktop')
# print(os.getcwd())

# Relative vs absolute path
# .\ && C:\\

# Creating new folders with os.makedirs()
# import os
# os.chdir('C:\\Users\\sukh\\Desktop')
# os.makedirs('.\Hello')

# os path modules || Handling absolute and relative path
# import os
# print(os.path.abspath('.'))
# print(os.path.abspath('.\\Scripts'))
# print(os.path.isabs('.'))
# print(os.path.relpath('C:\\Windows','C:\\'))
# print(os.path.relpath('C:\\Windows','C:\\spam\\eggs'))

# path = 'C:\\Windows\\System32\\calc.exe'
# print(os.path.basename(path))
# print(os.path.dirname(path))
# print(os.path.split(path))
# print(path.split(os.path.sep))
# print(path)

# Finding file size and folder contents
# import os
# print(os.path.getsize('C:\\Users'))
# totalsize = 0
# for filename in os.listdir('C:\\Users'):
#      totalsize = totalsize + os.path.getsize(os.path.join('C:\\Users',filename))
# print(totalsize)

# checking path validity
# import os
# print(os.path.exists('C:\\Windows'))
# print(os.path.exists('C:\\some__made__up_folder'))
# print(os.path.isdir('C:\\Windows\\System32'))
# print(os.path.isfile('C:\\Windows\\System32'))
# print(os.path.isdir('C:\\Windows\\System32\\calc.exe'))
# print(os.path.isfile('C:\\Windows\\System32\\calc.exe'))
# print(os.path.exists('D:\\'))

# File reading and writing process
# opening files with open() function
#helloFile = open('C:\\Users\\sukh\\Desktop\\hello.txt')
#helloContent = helloFile.read()
# print(helloContent)
#helloContent = helloFile.readlines()
#print(helloContent)

# Writing to files
# helloFile = open('C:\\Users\\sukh\\Desktop\\hello.txt')
# helloFile.write('Hello World!\n')
# helloFile = open('C:\\Users\\sukh\\Desktop\\hello.txt')
# print(helloFile.readlines())
# for x in helloFile.readlines():
#      x = x.replace('\n','')
#      z = '''            <recordTypeVisibilities>
#                <recordType>CanaryAMS__Insurance_Product__c.''' + x + '''</recordType>
#                <visible>true</visible>
#             </recordTypeVisibilities>'''
#      print(z)

# Saving variable to the shelve modules
# import shelve
# shelfFile = shelve.open('mydata')
# cats = ['Zophie','Pooka','Simon']
# shelfFile['cats'] = cats
# shelfFile.close()
# # print(type(shelve))
# shelfFile = shelve.open('mydata')
# print(list(shelfFile.keys()))
# print(list(shelfFile.values()))
# shelfFile.close()

# Saving variable with pprint.pformat

# import pprint,os

# cats = [{'name':'Zophie','desc':'chubby'},{'name':'Pooka','desc':'fluffy'}]
# os.chdir('C:\\Users\\sukh\\Desktop')
# fileObj = open('hello.py','w')
# fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
# print(open('hello.py'))
# fileObj.close


# Project generarting random quiz files

# randomquizgenerator.py

# import random,os

# This quiz data, keys are state and values are their capitals

'''

capitals =  {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'NewMexico': 'Santa Fe',
 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate 35 quiz files
os.chdir('C:\\Users\\sukh\\Desktop\\Python')
for quizNum in range(35):
# Create the quiz files and answer key files
     quizFile = open('capitalquiz%s.txt' % (quizNum + 1),'w')
     answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1),'w')
#  Write out the header for the quiz
     quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
     quizFile.write((' ' )*20 + 'State Capitals Quiz (Form %s)' %(quizNum + 1))
     quizFile.write('\n\n')
# Shuffle the order of the states
     states = list(capitals.keys())
     random.shuffle(states)
# Loop through all 50 states, making a question for each
     for questionNum in range(50):
          # Get the right and wrong answers
          correctAnswer = capitals[states[questionNum]]
          wrongAnswers = list(capitals.values())
          del wrongAnswers[wrongAnswers.index(correctAnswer)]          
          wrongAnswers = random.sample(wrongAnswers,3)
          answerOptions = wrongAnswers + [correctAnswer]
          random.shuffle(answerOptions)

          # Write the questions and answer options to the quiz files
          quizFile.write('%s. What is the capital of %s?\n' %(questionNum + 1,states[questionNum]))
          for i in range(4):
               quizFile.write('    %s. %s\n'%('ABCD'[i],answerOptions[i]))
               quizFile.write('\n')
          # Write the answer key to the file
          answerKeyFile.write('%s. %s\n' %(questionNum + 1,'ABCD'[answerOptions.index(correctAnswer)]))
     quizFile.close()
     answerKeyFile.close()
'''