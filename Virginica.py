#Brian Condon
#Trying to access just the virginica data
#23/4/18

import numpy 

#I created another csv file after having trouble splitting up the columns to just the setosa file.
data = numpy.genfromtxt('data/virginica.csv', delimiter = ',')

#Virginica Petal Length
virginpl = data[:,2]
meanvirginpl = numpy.mean(data[:,2])

#Virginica Petal Width
virginpw = data[:,3]
meanvirginpw = numpy.mean(data[:,3])

#excludes nan from the file so we can use numpy to develop mean etc. https://stackoverflow.com/questions/11620914/removing-nan-values-from-an-array
virginpl = virginpl[~numpy.isnan(virginpl)]

#Making a scatterplot
import matplotlib.pyplot as pl 
pl.scatter(virginpl,virginpw)
pl.show()

print("The mean petal length of the virginica is",meanvirginpl) #Answer is 5.5cm 
print("The mean petal width of the virginica is",meanvirginpw) #Answer is 2.0cm
