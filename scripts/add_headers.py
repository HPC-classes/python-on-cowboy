def addHeader(filename):
    '''
    addHeader(filename)

    Inputs: filename - string of path/name of csv file

    Outputs: rewrites csv file with headers

    Function adds headers for days and labels for inflammation files
    so that the inflammation .csv files are human-readable when openned
    inside a spreadsheet program.
    '''
    # open .csv file
    csvfile = open(filename)
    data = csvfile.read()
    csvfile.close()

    # process as a nested list
    data = data.split('\n')
    for i in range(0,len(data)):
        data[i] = data[i].split(',')
    days = len(data[0])
    data.remove([''])

    # create day headers
    header = ['Day ' + str(i) for i in range(1,days+1)]

    # create labels for data files
    cider = ['inflammation-' + str(i) for i in range(1,13)]
    cider.insert(0, '')
    cider.insert(len(cider), 'Overall:')

    # append header and labels to data
    data.insert(0, header)
    for i in range(0,len(data)):
        data[i].insert(0,cider[i])

    # put it all back together as a string
    for i in range(0,len(data)):
        data[i] = ','.join(data[i])
    data = '\n'.join(data)

    # write formatted output back to file
    csvfile = open(filename, 'w')
    csvfile.write(data)
    csvfile.close()
