import sys

def reducer():
    '''
    For every single unit, write a reducer that will return the busiest datetime (e.g.,
    the entry that had the most entries).  Ties should go to datetimes that are later on in the 
    Month of May.  You can assume that the contents of the reducer will be sorted by UNIT, such that
    all entries corresponding to a given UNIT will be sorted together. The output should be the UNIT
    name, the datetime (which is a concatenation of date and time), and ridership separated by tabs.

    For example, the output of the reducer may look like this:
    R001    2011-05-11 17:00:00    31213.0
    R002    2011-05-12 21:00:00    4295.0
    R003    2011-05-05 12:00:00    995.0
    R004    2011-05-12 12:00:00    2318.0
    R005    2011-05-10 12:00:00    2705.0
    R006    2011-05-25 12:00:00    2784.0
    R007    2011-05-10 12:00:00    1763.0
    R008    2011-05-12 12:00:00    1724.0
    R009    2011-05-05 12:00:00    1230.0
    R010    2011-05-09 18:00:00    30916.0
    ...
    ...
    
    '''

    entries = {}
    for line in sys.stdin:
        data = line.strip().split('\t')
        if len(data) != 4:
            continue
        else:
            key = data[0]
            riders = float(data[1])
            if key not in entries:
                entries[key] = [data[2]+ ' ' + data[3], riders]
            else:
                if entries[key][1] <= riders:
                    entries[key] = [data[2] + ' ' + data[3], riders]
    for key in entries:
        print (key + '\t' + str(entries[key][0]) + '\t' + str(entries[key][1]))

reducer()