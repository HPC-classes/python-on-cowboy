import numpy
import glob
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot
import os

if not os.path.exists('output'):
    os.makedirs('output')

data = numpy.loadtxt(fname='data/inflammation-01.csv', delimiter=',')
alldatamean = data.mean(axis=0)
alldatamax = data.max(axis=0)
alldatamin = data.min(axis=0)

filenames = glob.glob('data/inflammation*.csv')
filenames = filenames[1:]
for f in filenames:
    data = numpy.loadtxt(fname=f, delimiter=',')
    alldatamean = alldatamean + data.mean(axis=0)
    alldatamax = numpy.maximum(alldatamax, data.max(axis=0))
    alldatamin = numpy.minimum(alldatamin, data.min(axis=0))
print('all data mean is:', alldatamean/12)
print('all data max is:', alldatamax)
print('all data min is:', alldatamin)

fig = matplotlib.pyplot.figure(figsize=(10.0 ,3.0))

fig.suptitle('all the data')

axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.set_ylabel('average')
axes1.plot(alldatamean/12)

axes2.set_ylabel('max')
axes2.plot(alldatamax)

axes3.set_ylabel('min')
axes3.plot(alldatamin)

fig.tight_layout()

matplotlib.pyplot.savefig('output/alldata.pdf')

