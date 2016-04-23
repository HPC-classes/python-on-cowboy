# goal: calculate the average, max, and min inflammation per day
# across all patients 
import numpy
import glob
import os

# function used to make .csv data pretty once all the data is processed
from add_headers import addHeader

# setup directory for .csv output
if not os.path.exists('output'):
    os.makedirs('output')

# get file names for all the data files
filenames = glob.glob('data/inflammation*.csv')
print("filenames", filenames)
# setup lists for holding accumulated data
alldatamean = list()
alldatamax = list()
alldatamin = list()

for f in filenames:
    # import data and show status
    print(f)
    data = numpy.loadtxt(fname=f, delimiter=',')
    
    # convert data from arrays to lists so can append later
    meanAsList = data.mean(axis=0).tolist()
    maxAsList = data.max(axis=0).tolist()
    minAsList = data.min(axis=0).tolist()
    
    # print data for each specific file to standar output
    print("mean is:",'\n--------\n', meanAsList)
    print("\nmax is:",'\n-------\n', maxAsList)
    print("\nmin is:",'\n-------\n', minAsList, '\n\n')
    
    # append this file's data to the overall data
    alldatamean.append(meanAsList)
    alldatamax.append(maxAsList)
    alldatamin.append(minAsList)
    
# change back into array in order to enjoy numpy goodness
alldatamean = numpy.array(alldatamean)
alldatamax = numpy.array(alldatamax)
alldatamin = numpy.array(alldatamin)

# output overall data to standard output
print("\n\n\n\n*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*\n")
print("Overall Data by Day:\n\n")

'''
WARNING: This average only works because there are exactly
60 patients in every data file. If the number of patients
in each data file is not exactly the same, or if the 
number of patients is unkown for any given file then the
code must be changed to accommodate for a weighted average!
'''

# output mean, min, and max
print("mean is:",'\n--------\n', alldatamean.mean(axis=0))
print("\nmax is:",'\n-------\n', alldatamax.max(axis=0))
print("\nmin is:",'\n-------\n', alldatamin.min(axis=0), '\n\n')

''' 
append mean, min, and max to last row of array so the whole
thing can be written out to a .csv file
'''
alldatamean = numpy.vstack([alldatamean, alldatamean.mean(axis=0)])
alldatamax = numpy.vstack([alldatamax, alldatamax.max(axis=0)])
alldatamin = numpy.vstack([alldatamin, alldatamin.min(axis=0)])

# output results to csv
numpy.savetxt('output/mean.csv', alldatamean, fmt='%.2f', delimiter=',')
numpy.savetxt('output/max.csv', alldatamax, fmt='%.2f', delimiter=',')
numpy.savetxt('output/min.csv', alldatamin, fmt='%.2f', delimiter=',')

# make .csv files excel friendly
addHeader('output/mean.csv')
addHeader('output/max.csv')
addHeader('output/min.csv')
