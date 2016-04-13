import os
import numpy
import matplotlib
matplotlib.use('Agg')
import glob
import matplotlib.pyplot

if not os.path.exists('output'):
    os.makedirs('output')

filenames = glob.glob('data/inflammation*.csv')
filenames = filenames[0:3]
for f in filenames:
    print(f)
    data = numpy.loadtxt(fname=f, delimiter=',')
    print("after loadtxt")
    fig = matplotlib.pyplot.figure(figsize=(10.0 ,3.0))
    print("after figsize")

    fig.suptitle(f)
    #matplotlib.pyplot.title(f)
    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    axes1.set_ylabel('average')
    axes1.plot(data.mean(axis=0))

    axes2.set_ylabel('max')
    axes2.plot(data.max(axis=0))

    axes3.set_ylabel('min')
    axes3.plot(data.min(axis=0))

    # fig.tight_layout()
    # matplotlib.pyplot.show()
    outfile = 'output/'+f[5:20] +'.pdf'
    print(outfile)
    matplotlib.pyplot.savefig(outfile)
    
