#Brian Condon
#19/04/18
#Analysis of the second column of data in irisdata set

# import to analyse data
import numpy

# accessing data file https://docs.python.org/3/library/csv.html
data = numpy.genfromtxt('data/iris.csv', delimiter = ',') 

# accessing the second column https://stackoverflow.com/questions/15389290/how-to-find-out-the-average-on-a-csv-file 
secondcol = data[:,1] 
meansecondcol = numpy.mean(data[:,1]) 

minsecondcol = numpy.min(data[:,1])

maxsecondcol = numpy.max(data[:,1])

# Import to make histogram
import matplotlib.pyplot as pl

# Makes the graph, added labels using the pop up window
pl.hist(secondcol)
pl.show()

#Print out the results
print("The mean sepal width of the data set is",meansecondcol) #Answer is 3.054
print("The minimum sepal width of the data set is",minsecondcol) #Answer is 2.0
print("The maximum sepal width of the data set is",maxsecondcol) #Answer is 4.4

