# Brian Condon
# 19/4/18
# Analysing the first column of data 

# import numpy for analysis
import numpy 

# accessing data file https://docs.python.org/3/library/csv.html
data = numpy.genfromtxt('data/iris.csv', delimiter = ',')

# accessing the first column
firstcol = data[:,0]

#Calculating mean, min and max https://stackoverflow.com/questions/15389290/how-to-find-out-the-average-on-a-csv-file 
meanfirstcol = numpy.mean(data[:,0])
minfirstcol = numpy.min(data[:,0])
maxfirstcol = numpy.max(data[:,0])

# Import to make histogram
import matplotlib.pyplot as pl

# Makes the graph, added labels using the pop up window
pl.hist(firstcol)
pl.show() 

#import scatter plot showing the sepal length and width of the iris flower https://stackoverflow.com/questions/10336614/scatter-plot-in-matplotlib
# Added titles https://bespokeblog.wordpress.com/2011/07/07/basic-data-plotting-with-matplotlib-part-2-lines-points-formatting/
pl.scatter(firstcol,secondcol) 
pl.xlabel('Sepal Length in cms')
pl.ylabel('Sepal Width in cms')
pl.title('The Sepal Length and Width of the Iris Flower')
pl.show()
 
 #print out the results
print("The mean sepal length of the data set is", meanfirstcol) # Answer is 5.84
print("The minimum sepal length of the data set is", minfirstcol) # Answer is 4.3
print("The maximum sepal length of the data set is", maxfirstcol) #Answer is 7.9 


