# Brian Condon
# 19/4/18
# Calculating mean using Numpy 

# import numpy for analysis
import numpy 

# accessing data file
data = numpy.genfromtxt('data/iris.csv', delimiter = ',')

# accessing the first column
firstcol = data[:,0]

#Calculating mean, min and max
meanfirstcol = numpy.mean(data[:,0])
minfirstcol = numpy.min(data[:,0])
maxfirstcol = numpy.max(data[:,0])

# Import to make histogram
import matplotlib.pyplot as pl

# Makes the graph, added labels using the pop up window
pl.hist(firstcol)
pl.show() 

print("The mean sepal length of the data set is", meanfirstcol) # Answer is 5.84
print("The minimum sepal length of the data set is", minfirstcol) # Answer is 4.3
print("The maximum sepal length of the data set is", maxfirstcol) #Answer is 7.9 


