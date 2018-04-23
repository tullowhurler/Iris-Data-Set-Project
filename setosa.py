#Brian Condon
#Trying to access just the setosa data
#23/4/18

import numpy 

#I created another csv file after having trouble splitting up the columns to just the setosa file.
data = numpy.genfromtxt('data/setosa.csv', delimiter = ',')

setosa = data[:,0]

#excludes nan from the file so we can use numpy to develop mean etc. https://stackoverflow.com/questions/11620914/removing-nan-values-from-an-array
setosa = setosa[~numpy.isnan(setosa)]
print(setosa)
