#Brian Condon
#Trying to access just the setosa data
#23/4/18

#import to do analysis
import numpy 

#I created another csv file after having trouble splitting up the columns to just the setosa file.
data = numpy.genfromtxt('data/setosa.csv', delimiter = ',')

# Seperate the column
setosa = data[:,0]

meansetosa = numpy.mean((data[:,2]))
setosapw = data[:,3]

#excludes nan from the file so we can use numpy to develop mean etc. https://stackoverflow.com/questions/11620914/removing-nan-values-from-an-array
setosa = setosa[~numpy.isnan(setosa)]
print("The mean petal length of the setosa is",meansetosa)
