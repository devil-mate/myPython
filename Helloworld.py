#!/usr/bin/env python2.7
_metaclass_=type 
i=1
a=2;b=3

class ClassTest:
	def printhello():
		print "this is a class"
	
def fun01(a,b):
	#print "this is a function ,param is :",para1
	sum01=a+b
	return sum01
	
while i<10:
	print "hello world",i
	i+=1
'''
for i in range(1,20):
	print i             
'''
sum02=fun01(a,b)
print sum02
myclass=ClassTest()
myclass.printhello


	
	
	
