# Chapter 4 : List

# list Datatype
'''
        Methods : -> len,del,slice,concatation,changning values
    '''

# Working with lits

'''
    allMyCats1.py

catNames = []
while True:
     print('Enter the name of cat ' + str(len(catNames) + 1) + ' Or Enter nothing to stop : ')
     name = input()
     if(name == ''):
         break
     catNames = catNames + [name] # List concatation
     print('The cat names are: ')
for name in catNames :
    print(' ' + name)
     
'''

# Using for loop with list
'''
supplies = ['pen','stapler','flame-throwes','binders']
i = 0
for name in supplies:
    print('Index ' + str(i) + ' in supplies is : '  + name)
    i+=1
'''

# in and not in operator
'''
myPets  = ['Kutta','Kamina','Opposite']
print('Enter the Pet Name')
name = input()
if name not in myPets:
    print('Wrong House')
else:
    print('You found ' + name)
'''

# Multiple assignment tricks
'''
cat = ['Kutta','Kamina','Opposite']
spam , test,test1,test2 = cat
'''

# Argumented assignment operators


# Testing something
# def hello(x):
#     x = x / 2
#     return x

# x = 10
# hello(x)
# print(x)

# practice

# def changeListToString(someList):
#     string = ''
#     for i in someList:
#         string += i + ','
#     string = string[0:-1]
#     return string
    
# print(changeListToString(['Hello','World']))

grid =  [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for i in range(len(grid[0])):
    for z in range(len(grid)):
        print(grid[z][i],end='')
    print()
    
        
        