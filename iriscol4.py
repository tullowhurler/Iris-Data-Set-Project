#Brian Condon 
#Analysis of the fourth column of data
#20/04/18

# import to analyse data
import numpy 

# accessing data file
data = numpy.genfromtxt('data/iris.csv', delimiter = ',')

fourthcol = data[:,3]

meanfourthcol = numpy.mean(data[:,3])

minfourthcol = numpy.min(data[:,3])

maxfourthcol = numpy.max(data[:,3])

import matplotlib.pyplot as pl 
pl.hist(fourthcol)
pl.show()

print("The mean petal width of the data set it",meanfourthcol) #Answer 1.19cm
print("The minimum petal width of the data set is",minfourthcol) #Answer 0.1cm
print("The maximum petal width of the data set is",maxfourthcol) #Answer is 2.5cm
