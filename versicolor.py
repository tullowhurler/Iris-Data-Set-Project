#Brian Condon
#Trying to access just the versicolor data
#23/4/18

import numpy 

#I created another csv file after having trouble splitting up the columns to just the setosa file.
data = numpy.genfromtxt('data/versicolor.csv', delimiter = ',')

#Versicolor Petal Length
versicopl = data[:,2]
meanversicopl = numpy.mean(data[:,2])

#Versicolor Petal Width
versicopw = data[:,3]
meanversicopw = numpy.mean(data[:,3])

#excludes nan from the file so we can use numpy to develop mean etc. https://stackoverflow.com/questions/11620914/removing-nan-values-from-an-array
versicopl = versicopl[~numpy.isnan(versicopl)]

import matplotlib.pyplot as pl 
pl.scatter(versicopl,versicopw)
pl.show()

print("The mean petal length of the versicolor is",meanversicopl) #Answer is 4.2cm 
print("The mean petal width of the versicolor is",meanversicopw) #Answer is 1.3cm
