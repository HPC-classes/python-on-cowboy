import os
import numpy
import matplotlib
matplotlib.use('Agg')
import glob
import matplotlib.pyplot
from matplotlib.backends.backend_pdf import PdfPages

pdf_pages = PdfPages('multiple-inflammation.pdf')

if not os.path.exists('output'):
    os.makedirs('output')

filenames = glob.glob('data/inflammation*.csv')
#filenames = filenames[0:3]
for f in filenames:
    data = numpy.loadtxt(fname=f, delimiter=',')
    fig = matplotlib.pyplot.figure(figsize=(10.0 ,3.0))

    fig.suptitle(f)

    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    axes1.set_ylabel('average')
    axes1.plot(data.mean(axis=0))

    axes2.set_ylabel('max')
    axes2.plot(data.max(axis=0))

    axes3.set_ylabel('min')
    axes3.plot(data.min(axis=0))

    pdf_pages.savefig(fig)    
pdf_pages.close()

