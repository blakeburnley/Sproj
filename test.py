#Blake Burnley
#Senior Project
#Testing file for Python
import methodFinder

#Add line that creates the byte code from class file
#Try to automate as much as possible


#Select only the lines that have 'Method' in them
methodFinder.selectMethods("testByteCode.txt","Method","test.txt")

#Use this to get the actual method name: Is this needed?

#Use this to sort the lines alphabetically: Is this needed?


#Can tailor this for specific methods
#this is adding a new line character to the pattern
f = open("dangMethodCalls.txt","r")
out=open("output.txt", "w+")
for l in f:
	l = l[:-1]
	methodFinder.methodCounter("test.txt",l)
	out.write(l+",")
	out.write(str(methodFinder.methodCounter.lc))
	out.write(","+str(methodFinder.methodCounter.count))
	out.write(","+str(methodFinder.methodCounter.prop)+"\n")


f.close()
out.close()

