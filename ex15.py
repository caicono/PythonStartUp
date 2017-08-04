# -*- coding: cp936 -*-
from sys import argv

script,file_name = argv
prompt = '>'

txt = open(file_name)
print "Here is your file %r:" %file_name
print txt.read()

print "Type the file name again:"
file_again = raw_input('>')

txt2 = open(file_again)
print "Another file:"
print txt2.read()

file_content=""
line_sum = 5
i = 0
for i<line_sum:
	line = txt.readline()
	file_content = file_content + line
	i = i+1

print "Your file%s content is:" , file_content 