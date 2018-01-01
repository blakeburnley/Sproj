#Blake Burnley
#Senior Project
#Checking byte code for methods

from regex import *
import re


#Function that makes new file without lines that dont have pattern


#Function that removes everything that isn't the Method >is this needed



#Function that sorts it > is this needed?




#Basic regex search Function
#Run this in a loop with a file that has the patterns
def methodCounter(fileName,pattern):
	fh = open(fileName,"r")

	#attributes
	methodCounter.lc = 0
	methodCounter.count=0
	methodCounter.prop=0
	#pattern = 'java' #for some reason it is adding \n to pattern from file

	for l in fh:
	    methodCounter.lc +=1
	    if (re.search(pattern,l)):
	        methodCounter.count +=1
	        print(l)

	#calculate the proportion
	methodCounter.prop=(methodCounter.count/methodCounter.lc)
	fh.close()








