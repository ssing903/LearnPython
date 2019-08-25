#! python3
# renameDates.py - Renames filenames with american MM-DD-YYYY date format
# to European DD-MM-YYYY.

import shutil,os,re

# Create a regex that match american date format
datePattern = re.compile(r"""^(.*?)      # alltext before date
                         ((0|1)?\d)-     # one or two digits for the month
                         ((0|1|2|3)?\d)- #one or 2 digits for the day
                         ((19|20)\d\d)   #four digits for the year
                         (.*?)$          # all the text after the date
                         """,re.VERBOSE)

# Loop over files in working directory
os.chdir('C:\\Users\\sukh\\Desktop\\Ishrat')
for amerFileName in os.listdir('.'):
     mo = datePattern.search(amerFileName)

# skip files without a date
     if mo == None:
          continue
     
# Get different parts of the filename
     beforepart = mo.group(1)
     monthpart = mo.group(2)
     daypart = mo.group(4)
     yearpart = mo.group(6)
     afterpart = mo.group(8)

# form the european-style filename
     euroFilename = beforepart + daypart + '-' + monthpart + '-' + yearpart + afterpart
# Get the full absolute paths
     absWorkingDir = os.path.abspath('.')
     amerFileName = os.path.join(absWorkingDir,amerFileName)
     euroFilename = os.path.join(absWorkingDir,euroFilename)
# rename the files
     print('Renaming "%s" to "%s"...'%(amerFileName,euroFilename))
     shutil.move(amerFileName,euroFilename)
