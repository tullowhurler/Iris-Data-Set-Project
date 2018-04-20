#Brian Condon 
#Analysis of the third column of data
#20/04/18

# import to analyse data
import numpy 

# accessing data file
data = numpy.genfromtxt('data/iris.csv', delimiter = ',')

thirdcol = data[:,2]

meanthirdcol = numpy.mean(data[:,2])
