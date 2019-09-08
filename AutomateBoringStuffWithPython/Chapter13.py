# Chapter 13 - working with pdf and stuff 

import os,PyPDF2

'''
os.chdir('C:\\Users\\Sukh\\Desktop\\automate_online-materials')
pdfFileObj = open('meetingminutes.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# print(pdfReader.getPage(1).extractText())
# print(pdfReader.numPages)

print('========================')
for i in range(pdfReader.numPages):
	print(pdfReader.getPage(i).extractText())
	print('Page ' + str(i) + ' ends here')
	print()
print('========================')
'''
# Decrypting PDF
'''
pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf','rb'))
# print(pdfReader.isEncrypted)
pdfReader.decrypt('rosebud')
print(pdfReader.getPage(0))
'''

# Creating Pdf and stuff

'''
os.chdir('C:\\Users\\Sukh\\Desktop\\automate_online-materials')

pdf1Reader = PyPDF2.PdfFileReader(open('meetingminutes.pdf','rb'))
pdf2Reader = PyPDF2.PdfFileReader(open('meetingminutes2.pdf','rb'))

pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdf1Reader.numPages):
	pageObj = pdf1Reader.getPage(pageNum)
	pdfWriter.addPage(pageObj)

for pageNum in range(pdf2Reader.numPages):
	pageObj = pdf2Reader.getPage(pageNum)
	pdfWriter.addPage(pageObj)

os.chdir('C:\\Users\\Sukh\\Desktop')
pdfOutputFile = open('combinedMinutes.pdf','wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
os.chdir('C:\\Users\\Sukh\\Desktop\\automate_online-materials')
open('meetingminutes.pdf','rb').close()
open('meetingminutes2.pdf','rb').close()
'''

# Combining Select Pages from Many pdf
os.chdir('C:\\Users\\Sukh\\Desktop\\automate_online-materials')

