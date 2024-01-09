# Metabolite Annotation but more np to run faster

import numpy as np
from itertools import product

with open("3.txt", "r") as input_file:
    alllines = input_file.read().splitlines()
    alllines.pop(0)

outF = open("output.txt", "w")
for linepos in range(len(alllines)):
    if linepos % 4 == 0:
        M, N, K = alllines[linepos+1], alllines[linepos+2], alllines[linepos+3]
        M, N, K = M.split(" "), N.split(" "), K.split(" ")

        M = [x for x in M if x]
        N = [x for x in N if x]
        K = [x for x in K if x]
        
        # create matrix of m by n:
        sumsarray = np.array([float(x) + float(y) for x, y in product(M, N)]).reshape(len(M), len(N))

        sumsarray1 = np.where(sumsarray > 0, sumsarray, sumsarray*100)

        for k in K:
            test = abs(sumsarray1 - float(k))
            ind1, ind2 = list(np.unravel_index(np.argmin(test, axis=None), test.shape))
            ind1, ind2 = int(ind1)+1, int(ind2)+1

            outF.write(f"{ind1} {ind2}" + '\n')

outF.close()

print("end")
