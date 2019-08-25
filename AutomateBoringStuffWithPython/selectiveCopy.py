#! python3
# selectiveCopy.py for selecting type of files 

import os,shutil,re

# search all the files in tree with .jpg or .pdf

def searchFile(fromFolder,toFolder):
     
     # serach for pattern
     jpgPattern = re.compile('txt$')
     # walk through all the tree
     fromFolder = os.path.abspath(fromFolder)
     
     for jpgFile in os.listdir(fromFolder):
          if jpgFile.endswith('.txt'):
               shutil.copy(fromFolder+'\\'+jpgFile,toFolder)

searchFile('C:\\Users\\sukh\\Desktop\\Python','C:\\Users\\sukh\\Desktop\\Ishrat')