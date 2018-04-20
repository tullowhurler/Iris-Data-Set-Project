 #Brian Condon 
#Analysis of the third column of data
#20/04/18

# import to analyse data
import numpy 

# accessing data file https://docs.python.org/3/library/csv.html
data = numpy.genfromtxt('data/iris.csv', delimiter = ',')

# Access the third column https://stackoverflow.com/questions/15389290/how-to-find-out-the-average-on-a-csv-file 
thirdcol = data[:,2]
meanthirdcol = numpy.mean(data[:,2])

minthirdcol = numpy.min(data[:,2])

maxthirdcol = numpy.max(data[:,2])

#import to make the histogram
import matplotlib.pyplot as pl 

# lable the histogram and print the result 
pl.hist(thirdcol)
pl.show()

# created scatterplot https://stackoverflow.com/questions/10336614/scatter-plot-in-matplotlib
pl.scatter(thirdcol,fourthcol)
pl.show()

#print the outcome
print("The mean petal length of the data set it",meanthirdcol) #Answer 3.75cm
print("The minimum petal length of the data set is",minthirdcol) #Answer 1.0cm
print("The maximum petal length of the data set is",maxthirdcol) #Answer is 6.9cm
