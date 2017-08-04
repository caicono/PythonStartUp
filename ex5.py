# -*- coding: utf-8 -*-

#my_name = 'caicono'
my_name = "caicono"
my_age = 35
my_height = 172
my_weight = 130

print "Let us talk about %s" % my_name
print "How old are you ? I am %s " % my_age, "years old" 
print 'What is sum of all your age: %d ,weight: %d ,height: %d ? The answer is: %d' % (
my_age,my_weight,my_height,my_age+my_weight+my_height)


##ex7
print "." * 10


##ex8

formatter = "%r %r %r %r "
print formatter % ('I had this thing' ,'that you type right', 'but it did not sing', 'So I said good night')


##ex10
##while True:
##	for i in ["/","-","\\","|"]:
##		print "%s\r" % i

for i in [1,2,3,4,5]:
	print "This is %d times" % i