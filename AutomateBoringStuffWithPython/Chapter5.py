# Dictionaries and structuring data
# myCat = {'size':'fat','color':'gray','dispostion':'loud'}
# print(myCat)

# Dictionaries VS Lists
# spam = ['cats','dogs','moose'] # ordered vs unordered

# spam = ['cats','dogs','moose']
# bacon = ['dogs','cats','moose']
# print(spam==bacon)

# spam = {'name':'Sukh','age':10}
# bacon = {'age':10,'name':'Sukh'}
# print(spam==bacon)

# birthdays.py
# birthdays  = {'Alice':'Apr1','Bob':'Dec 12','Carol':'Mar 4'}
# while True:
#      print('Enter a name : (blank to quit)')
#      name = input()
#      if(name == ''):
#           break
     
#      if name in birthdays:
#           print(birthdays[name] + ' is the birthdays of ' + name)
#      else:
#           print('I dont have birthdays information for ' + name)
#           print('What their birthdays?')
#           bday = input()
#           birthdays[name] = bday
#           print('Birthday database updated')

# Keys values and items methods
# spam = {'color':'red','age':42}
# for v in spam.values():
#      print(v)
# print('===========')
# for v in spam.keys():
#      print(v)
# print('===========')
# test  = spam.items();
# for v in test:
#      print(list(v))

# spam = {'color':'red','age':42}
# for k,v in spam.items():
#      print('Key: ' + k + ' Value: ' +str(v))

# checking whether key exist in Dictionary
# spam = {'name':'Zophie','age':7}
# print(('name','Zophie') in spam.items())

# The get() methods
# picnicItems = {'apples':5,'cups':2}
# print('I am bringing ' + str(picnicItems.get('cups',0))  + ' cups.')
# print('I am bringing ' + str(picnicItems.get('eggs',0))  + ' eggs.')

# Setdefault() methods
# spam = {'name':'Pooka','age':5}
# print(spam)
# spam.setdefault('color','black')
# print(spam)
# spam.setdefault('color','white')
# print(spam)
# spam['color'] = 'white'
# print(spam)

# charactercount.py

# message = 'It was a bright day cold day in April, and the clocks were striking thirteen.'
# count = {}

# for character in message:
#      count.setdefault(character,0)
#      count[character] = count[character] + 1
# print(count)

# pretty writing
# prettycharacterCount.py

# import pprint
# message = 'It was a bright day cold day in April, and the clocks were striking thirteen.'
# count = {}
# for character in message:
#      count.setdefault(character,0)
#      count[character] = count[character] + 1
# #pprint.pprint(count)
# print(pprint.pformat(count))
# # print(str(len(count)))
# # print(str(len(message)))

# ticTacToe.py
# theBoard = {'top-L':' ','top-M':' ','top-R':' ',
#              'mid-L':' ','mid-M':' ','mid-R':' ',
#              'low-L':' ','low-M':' ','low-R':' '
#            }

# def printBoard(board):
#      print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
#      print('-+-+-')
#      print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
#      print('-+-+-')
#      print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

# printBoard(theBoard)

# turn = 'X'
# for i in range(9):
#      printBoard(theBoard)
#      print('Turn for ' + turn + ' . Move on which space?')
#      move = input()
#      theBoard[move] = turn
#      if turn == 'X':
#           turn = '0'
#      else:
#           turn = 'X'
# printBoard(theBoard)

# nested dictionaries and list
# total bought()

# allGuests = {'Alice' :{'apples' : 5, 'pretzels':12},
#               'Bob' : {'ham':3,'apples':2},
#               'Carol':{'cups':3,'apple pies' :1}
#             }

# def totalBought(guests,item):
#      numBought = 0
#      for k,v in guests.items():
#           numBought = numBought + v.get(item,0)
#      return numBought

# # print('Number of things being bought:')
# print('Apples  ' + str(totalBought(allGuests,'apples'))) 

# fanatsygame.py
# playerData = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def displayInventory(data):
     print('Inventory: ')
     items_total = 0
     for i in data.keys():
          print(str(data[i]) + ' ' + i)
          items_total += data[i]
     print(str(items_total))
# list to dictionary for fanatsy games

def addToInventory(Inventory,newList):
     x = 0
     for k in newList:
          if(k in Inventory):
               Inventory[k] = Inventory[k] + 1
          else:
               Inventory.setdefault(newList[x],1)
          #print(k + ' ' + str(Inventory[k]))
          x+=1
     return Inventory

inv  = {'gold coin' :42,'rope':1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
dragonLoot1 = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = addToInventory(inv,dragonLoot)
#print(inv)
displayInventory(inv)
inv = addToInventory(inv,dragonLoot)
displayInventory(inv)




