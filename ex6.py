# -*- coding: cp936 -*-
num = 10
x =  "There are %d types of people" % num
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary,do_not)

print x
print y

print "I said %r." % x

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

