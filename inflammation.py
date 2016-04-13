# goal: calculate the average, max, and min inflammation per day
# across all patients 
import numpy
import glob

filenames = glob.glob('data/inflammation*.csv')
filenames = filenames[0:3]
for f in filenames:
    print(f)
    data = numpy.loadtxt(fname=f, delimiter=',')
    print("mean is",data.mean(axis=0))
    print(data.max(axis=0))
    print(data.min(axis=0))
    
