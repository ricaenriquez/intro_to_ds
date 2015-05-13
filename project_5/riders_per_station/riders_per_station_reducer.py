import sys

def reducer():
    '''
    Given the output of the mapper for this exercise, the reducer should return one row
    per unit, along with the total number of ENTRIESn_hourly over the course of may. 
    
    You can assume that the input to the reducer is sorted by UNIT, such that all rows 
    corresponding to a particular UNIT are group together.

    '''
    
    entries = {}
    for line in sys.stdin:
        data = line.strip().split('\t')
        if len(data) != 2:
            continue
        else:
            key = data[0]
            if key not in entries:
                entries[key] = float(data[1])
            else:
                entries[key] += float(data[1])
    for key in entries:
        print (key + '\t' + str(entries[key]))

reducer()
