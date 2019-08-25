#! python3
# chapter10 Debugging 

# Raising Exceptions

# raise Exception('This is a error message')

'''
def boxPrint(symbol,width,height):
     if len(symbol) != 1:
          raise Exception('Symbol must be a single character string')
     if width <= 2:
          raise Exception('Width should be greater than 2')
     if height <= 2:
          raise Exception('Height should be greater than 2')
     print(symbol * width)
     for i in range(height -2):
          print(symbol + (' ' * (width -2) + symbol))
     print(symbol * width)

for sym, w, h in (('*',4,4),('0',20,5),('x',1,3),('ZZ',3,3)):
     try:
          boxPrint(sym,w,h)
     except Exception as err:
          print('An exception happend ' + str(err))
'''

# Getting traceback as string

'''
def spam():
     bacon()

def bacon():
     raise Exception('This is an exception messgae')

spam()
'''

# import traceback
# try:
#      raise Exception('This is an exception')
# except:
#      print(traceback.format_exc())

# Assertions - sanity check

# status = 'open'
# assert status == 'open','Door is open'
# status = 'close'
# assert status == 'open','Please open the door'

# Traffic light stmiulation

market_2nd = {'ns':'green','ew':'red'}
mission_16th = {'ns':'red','ew':'green'}

def switchLights(stoplight):
     for key in stoplight.keys():
          if stoplight[key] == 'green':
               stoplight[key] = 'yellow'
          elif stoplight[key] == 'yellow':
               stoplight[key] = 'red'
          elif stoplight[key] == 'red':
               stoplight[key] = 'green'
     
     assert 'red' in stoplight.values(),'Neither light is red! ' + str(stoplight)
switchLights(market_2nd)      


