import sys
import string

def mapper():
    """
    Each line in sys.stdin will be a line from a csv file representing the contents
    of our final Subway-MTA dataset.  For each line, this mapper should return the following:
    The unit, the ENTRIESn_hourly, the DATEn, and TIMEn columns, separated by tabs.  
    Example:

    R001    100000.0    2011-05-01  01:00:00
    """


    for line in sys.stdin:
        data = line.strip().split(',')
        if data[0] == "" or len(data) !=22:
            continue
        else:
            print (data[1] + '\t' + data[6] + '\t' + data[2] + '\t' + data[3])

mapper()