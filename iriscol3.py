#Brian Condon 
#Analysis of the third column of data
#20/04/18

# import to analyse data
import numpy 

# accessing data file
data = numpy.genfromtxt('data/iris.csv', delimiter = ',')

thirdcol = data[:,2]

meanthirdcol = numpy.mean(data[:,2])

minthirdcol = numpy.min(data[:,2])

maxthirdcol = numpy.max(data[:,2])

import matplotlib.pyplot as pl 
pl.hist(thirdcol)
pl.show()

print("The mean petal length of the data set it",meanthirdcol) #Answer 3.75cm
print("The minimum petal length of the data set is",minthirdcol) #Answer 1.0cm
print("The maximum petal length of the data set is",maxthirdcol) #Answer is 6.9cm
