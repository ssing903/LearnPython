 # Chapter 9 Organising files

 # The shutil modules
# import shutil,os

 # copying files and folders

# os.chdir('C:\\Users\\sukh\\Desktop\\Python')
# shutil.copytree('C:\\Users\\sukh\\Desktop\\Ishrat','C:\\Users\\sukh\\Desktop\\Python')

# moving and renaming files
# os.chdir('C:\\Users\\sukh\\Desktop\\Ishrat')
# shutil.move('new1.txt','C:\\Users\\sukh\\Desktop\\Python')


# Permanently deleting the files and folders
# pip3 send2trash
# import os
# for filename in os.listdir():
#  if filename.endswith('.rxt'):
#  #os.unlink(filename)
#  print(filename)

# Walking a directory tree
# import os

# for folderName, subFolders,fileNames in os.walk('C:\\Users\\sukh\\Desktop'):
#      print('The current folder is ' + folderName)
#      for subFolder in subFolders:
#           print('The subfolders of ' + folderName + ' is '  + subFolder)
#      for fileName in fileNames:
#           print('FILE INSIDE ' + folderName + ' : ' + fileName)
#      print('')


# compressing files with zipfile modules
# import os,zipfile

# os.chdir('C:\\Users\\sukh\\Desktop')
# exampleZip = zipfile.ZipFile('Python.zip')
# print(exampleZip.namelist())
# print(exampleZip.getinfo('Python/new1.txt').compress_size)
# exampleZip.close()

# Project renaming files with american style dates to european styles
