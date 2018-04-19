#Brian Condon
#19/04/18
#Analysis of the second column of data in irisdata set

import numpy

data = numpy.genfromtxt('data/iris.csv', delimiter = ',') 

secondcol = data[:,1] 

meansecondcol = numpy.mean(data[:,1])

print("The mean sepal width of the data set is",meansecondcol) #Answer is 3.054

