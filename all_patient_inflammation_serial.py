# goal: calculate the average, max, and min inflammation per day
# across all patients 
import numpy
import glob

#get file names for all the data files
filenames = glob.glob('data/inflammation*.csv')

#setup lists for holding accumulated data
alldatamean = list()
alldatamax = list()
alldatamin = list()

for f in filenames:
    #import data and show status
    print(f)
    data = numpy.loadtxt(fname=f, delimiter=',')
    
    #convert data from arrays to lists so can append later
    meanAsList = data.mean(axis=0).tolist()
    maxAsList = data.max(axis=0).tolist()
    minAsList = data.min(axis=0).tolist()
    
    #print data for each specific file
    print("mean is:",'\n--------\n', meanAsList)
    print("\nmax is:",'\n-------\n', maxAsList)
    print("\nmin is:",'\n-------\n', minAsList, '\n\n')
    
    #append this file's data to the overall data
    alldatamean.append(meanAsList)
    alldatamax.append(maxAsList)
    alldatamin.append(minAsList)
    
#change back into array in order to enjoy numpy goodness
alldatamean = numpy.array(alldatamean)
alldatamax = numpy.array(alldatamax)
alldatamin = numpy.array(alldatamin)

#output overall data
print("\n\n\n\n*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*\n")
print("Overall Data by Day:\n\n")

'''
WARNING: This average only works because there are exactly
60 patients in every data file. If the number of patients
in each data file is not exactly the same, or if the 
number of patients is unkown for any given file then the
code must be changed to accommodate for a weighted average!
'''

print("mean is:",'\n--------\n', alldatamean.mean(axis=0))
print("\nmax is:",'\n-------\n', alldatamax.max(axis=0))
print("\nmin is:",'\n-------\n', alldatamin.min(axis=0), '\n\n')
