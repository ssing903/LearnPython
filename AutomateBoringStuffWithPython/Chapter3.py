'''
This chapter is all about functions in python
Function
'''

'''
print('Hello World')


for i in range(5):
    if (i != 3):
     print(len(str(i)))
'''

# Functions

'''
def helloWorld(num1,num2) :
	total = num1 + num2
	print(total)

print('helloWorld')
num1 = input()
num2 = input()
helloWorld(int(num1),int(num2))
'''


# return statement
'''
import random

def getAnswer(answerNumber):
        if answerNumber == 1:
                return 'Its Certain'
        elif answerNumber == 2:
                return 'Its 2'
        elif answerNumber == 3:
                return 'Its 3'
        elif answerNumber == 4:
                return 'Its 4'
        elif answerNumber == 5:
                return 'It\'s 5'

RandomNumber = random.randint(1,5)
print(getAnswer(RandomNumber))
'''

'''
# Python keyword and aerguments in function
print('Hello','World',sep=',')
'''

'''
# Local And Global scope
    #Local Variable can't be used in global scope
eggs = 123
def spam():
    eggs = 31337;
    print(eggs)
spam()
print(eggs)

# Local variables can't use variables in the other local scope
def spam():
    eggs = 99
    bacon()
    print('Eggs of spam : ' + str(eggs))

def bacon():
    ham = 101
    eggs=0
    print('Eggs of bacon : ' + str(eggs));
spam()


# Global variables can be read from Local scope
def spam():
    print(eggs)
eggs = 42
spam()
print(eggs)
'''

'''
# Global statement
eggs = 'global'
print(eggs)
def spam():
    global eggs
    eggs = 'spam'

spam()
print(eggs)
'''

'''
# Final touch point
eggs = input()
def spam():
    global eggs
    eggs = 'Eggs inside spam' # this is global
def bacon():
    eggs = 'Eggs inside bacon' # this is local
def ham():
    print('Printing inside ham ' + eggs) #This is global
print('Before Spam : ' + str(eggs))
spam()
print('After spam : ' + str(eggs))
ham()
'''

'''
# Exception Handling
def spam(diviby):
    try:
        return 42/diviby
    except ZeroDivisionError:
        print('Error : invalid Argument.')

print(spam(2))
print(spam(0))
'''

'''
# Exception handling everywhere
def spam(divide):
    return 42 / divide
try:
    print(spam(2))
    print(spam(0))
    print(spam(2))
except ZeroDivisionError:
    print('Error : invalid argument')
'''

'''
# Short program guess the number
import random
secrectNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20')

# Ask the player to guess 6 time
for guessTaken in range(1,7):
    print('Take a guess')
    guess = int(input())

    if(guess < secrectNumber):
        print('Your Guess is too low')
    elif (guess > secrectNumber):
        print('Your Guess is too high')
    else:
        break
if (guess == secrectNumber):
    print('Good job ! You guessed in ' + str(guessTaken) + ' guess!')
else:
    print('Nope. The number i was thinking of was ' + str(secrectNumber))
'''


# Practice collatz program

def collatz(number):
    if(number % 2 == 0):
        return number / 2
    elif (number % 2 == 1):
        return (3 * number + 1)



try :
    number = int(input())
    while number != 1:

        number = collatz(number)
        print(str(number))
except ValueError :
        print('Please enter integer')
      
