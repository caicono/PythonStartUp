from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copy file:%s to another file:%s" %(from_file,to_file)

in_file = open(from_file)
in_data = in_file.read()

print "The input file is %s bytes long." % len(in_data)

print "Does output file exist? %r" % exists(to_file)
print "ready, hit RETURN to countinue, CTRL C to abort"
raw_input()

out_file = open(to_file,'w')
out_file.write(in_data)

print("Alright, please check it in your directory.")


in_file.close()
out_file.close()