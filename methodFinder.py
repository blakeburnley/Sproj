#Blake Burnley
#Senior Project
#Checking byte code for methods

from regex import *
import re


#Function that makes new file without lines that dont have pattern
def selectMethods(fileName,pattern,outfile):
	fh = open(fileName,"r")
	of = open(outfile, "w+")

	#loop
	for l in fh:
	    if (re.search(pattern,l)):
	    	#of.write(l)
	    	m = re.search("(Method).+",l)
	    	of.write(m.group(0)+"\n")
	#close file
	fh.close()
	of.close()


#Function that removes everything that isn't the Method 
#	>is this needed? Part of prior function
#Function that sorts it 
#	> is this needed? No

#Basic regex search Function
#Run this in a loop with a file that has the patterns
def methodCounter(fileName,pattern):
	fh = open(fileName,"r")

	#attributes
	methodCounter.lc = 0
	methodCounter.count=0
	methodCounter.prop=0
	#pattern = 'java' #for some reason it is adding \n to pattern from file

	#loop
	for l in fh:
	    methodCounter.lc +=1
	    if (re.search(pattern,l)):
	        methodCounter.count +=1
	        print(l)

	#calculate the proportion
	methodCounter.prop=(methodCounter.count/methodCounter.lc)
	fh.close()








