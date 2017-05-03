import fileinput
import os,sys

#insert name of folder that contains xml files
_XML_FILE_PATH = 'Annotations'
searchExp="  "
replaceExp="\t"
for _,_,files in os.walk(_XML_FILE_PATH):
	for i in files:
		directory=_XML_FILE_PATH+"/"+i
		#print directory
		input=fileinput.FileInput(directory,inplace=1)
		for line in input:
			if searchExp in line:
				line=line.replace(searchExp,replaceExp)
			sys.stdout.write(line)

