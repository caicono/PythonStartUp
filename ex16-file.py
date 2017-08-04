# -*- coding: cp936 -*-
from sys import argv

print "Type the file name again:"
file_again = raw_input('>')

txt2 = open(file_again)

file_content=""
line_sum = 9
i = 0
for i in range(0,line_sum):
	line = txt2.readline()
	file_content = file_content + line


print "Your file%s content is:\n%s" %(file_again, file_content) 