#! python3
# backupToZip.py - copies and entire folder and its contents into a zip file whose filename increments

import zipfile, os,sys

def backupToZip(folder):
     
     # backuo the entire contents of "folder" into zip file
     os.chdir('C:\\Users\\sukh\\Desktop')
     folder = os.path.abspath(folder)   # make sure folder is absolute

     # figure out the filename this code should use based on
     # what file already exists
     number = 1
     while True:
          zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
          if not os.path.exists(zipFilename):
               break
          number = number + 1
     print(zipFilename)
     
     # Create Zip file
     print('Creating %s...' %(zipFilename))
     backupZip = zipfile.ZipFile(zipFilename,'w')
     # Walk the entire folder tree and compress the files in each folder
     for foldername,subfolders,filenames in os.walk(folder):
          print('Adding files in %s....' %(foldername))
          # Add the current folder to zip file
          backupZip.write(foldername)
          # Add all the files in this folder zip file
          for filename in filenames:
               newBase = os.path.basename(folder) + '_'
               if filename.startswith(newBase) and filename.endswith('.zip'):
                    continue
               backupZip.write(os.path.join(foldername,filename))
     backupZip.close()
     print('Done.')
          
backupToZip(sys.argv[1])
