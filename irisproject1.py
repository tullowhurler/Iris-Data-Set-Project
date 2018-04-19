# Brian Condon
# 19/4/18
# Calculating mean using Numpy 

# import numpy for analysis
import numpy 

# accessing data file
data = numpy.genfromtxt('data/iris.csv', delimiter = ',')

# accessing the first column
firstcol = data[:,0] 
meanfirstcol = numpy.mean(data[:,0])

print("The mean sepal length of the data set is", meanfirstcol) 

# Answer is 5.84
