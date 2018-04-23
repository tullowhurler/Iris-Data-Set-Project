#Brian Condon
#Trying to access just the setosa data
#23/4/18

import numpy 

data = numpy.genfromtxt('data/iris.csv', delimiter = ',')

setosa = data[0:50]

print(setosa)
