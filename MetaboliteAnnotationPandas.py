# Metabolite Annotation but pandas to run faster

import pandas as pd
import numpy as np
from itertools import product

with open("4.txt", "r") as input_file:
    alllines = input_file.read().splitlines()
    del alllines[:5]

outlog= open("log.txt", "w")
outF = open("output.txt", "w")
for linepos in range(len(alllines)):

    cycle = 0
    if linepos % 4 == 0:
        cycle +=1
        M, N, K = alllines[linepos+1], alllines[linepos+2], alllines[linepos+3]
        M, N, K = M.split(" "), N.split(" "), K.split(" ")

        M = [x for x in M if x]
        N = [x for x in N if x]
        K = [x for x in K if x]

        outlog.write(f"Extracted M,N,K for cycle {cycle}." + '\n')
        
        df = pd.DataFrame(columns=list(range(1, len(N)+1)))

        count = 1
        for m in M:
            temp = []
            for n in N:
                sums = float(m)+float(n)
                if sums  > 0:
                    temp.append(sums)
                else:
                    temp.append(6000)
            newrow = pd.DataFrame([temp], columns=list(range(1, len(N)+1)))
            df = pd.concat([df, newrow], ignore_index=True)
            count = count+1
            outlog.write(f"Added {count} rows to dataframe, cycle {cycle}." + '\n')

        outlog.write(f"Completed dataframe for cycle {cycle}."+'\n')

        for k in K:
            df1 = abs(df-float(k))
            a, b = df1.stack().astype(float).idxmin()
            outlog.write(f"{a+1} {b}" + '\n')

outlog.close()
outF.close()
print("end")
        
            
