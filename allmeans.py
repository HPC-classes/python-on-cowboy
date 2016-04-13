#this works on jupyter


import numpy
import glob
import matplotlib.pyplot
% matplotlib inline
data = numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')
alldatamean = data.mean(axis=0)

filenames = glob.glob('inflammation*.csv')
filenames = filenames[1:-1]
# alldatamean = [[]]
for f in filenames:
    print(f)
    data = numpy.loadtxt(fname=f, delimiter=',')
    # print("mean is", data.mean(axis=0))
    #alldatamean = data.mean(axis=0)
    #print("max is", data.max(axis=0))
    #print("min is", data.min(axis=0))
    alldatamean = numpy.vstack([alldatamean,data.mean(axis=0)])
print('all data mean is:', alldatamean.mean(axis=0))

alldatamean_plot = matplotlib.pyplot.plot(alldatamean.mean(axis=0))
matplotlib.pyplot.show()

