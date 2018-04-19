#Brian Condon
#19/04/18
#Analysis of the second column of data in irisdata set

import numpy

data = numpy.genfromtxt('data/iris.csv', delimiter = ',') 

secondcol = data[:,1] 

meansecondcol = numpy.mean(data[:,1])
minsecondcol = numpy.min(data[:,1])

maxsecondcol = numpy.max(data[:,1])

print("The mean sepal width of the data set is",meansecondcol) #Answer is 3.054
print("The minimum sepal width of the data set is",minsecondcol) #Answer is 2.0
print("The maximum sepal width of the data set is",maxsecondcol) #Answer is 4.4

