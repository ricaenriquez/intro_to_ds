import sys
def reducer():

    aadhaar_generated = 0
    old_key = None

    #Cycle through the list of key-value pairs emitted
    #by your mapper, and print out each key once,
    #along with the total number of Aadhaar generated,
    #separated by a tab.  Assume that the list of key-
    #value pairs will be ordered by key.  Make sure
    #each key-value pair is formatted correctly!
    #Here's a sample final key-value pair: "Gujarat\t5.0"
    district_keys = {}
    
    for line in sys.stdin:
        data = line.strip().split('\t')
        if len(line) == 2:
            key = data[0]
            if key not in district_keys.keys():
                district_keys[key] = int(data[1])
            else:
                district_keys[key] += int(data[1])
    for key in district_keys:
        print key +'t' + district_keys[key]

    
reducer()