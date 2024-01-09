# Qualification round: Welcome section

with open("input.txt", "r") as input_file:
    alllines = input_file.read().splitlines()
    alls = alllines[1::2]
    allt = alllines[2::2]

    alltests = dict(zip(alls, allt))

def find_all(master, sub):
    start = 0
    while True:
        start = master.find(sub, start)
        if start == -1: return
        yield start
        start += 1
        # Use as part of list as with example below

for s, t in alltests.items():
    print(str([i+1 for i in list(find_all(s, t))]).replace(',', '').strip('[').strip(']'))


# Qualification round: Epigenomic Marks
import numpy as np
import tqdm
with open("2.txt", "r") as input_file:
    alllines = input_file.read().splitlines()
    alllines.pop(0)

linepos=0
outF = open("output.txt", "w")
for line in alllines:
    if ' ' in line:
        r = int(line.split(' ')[0])
        test = np.column_stack(list(l) for l in alllines[linepos+1:linepos+1+r])
            #print(test)

        unique_rows = np.unique(test, axis=0)
            
        statesindex = {}
        for i in range(len(unique_rows)):
            statesindex[str(unique_rows[i])] = i+1
                #print (stateindex)

        stateslist = []
        for s in test:
            state = statesindex[str(s)]
            stateslist.append(state)
            

        #print(len(statesindex))
        #print(str(stateslist).replace(',', '').strip('[').strip(']'))
        outF.write(str(len(statesindex)) + '\n')
        outF.write(str(stateslist).replace(',', '').strip('[').strip(']') + '\n')

        linepos += (1+r)
outF.close()
