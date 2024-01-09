# Qualification round: Metabolite Annotation

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

        allsums = [float(x) + float(y) for x, y in product(M, N)]
        allpairs = list(product(M, N))
        sumsindex = dict(zip(allsums,allpairs))

        for k in K:
            diff = []
            temp = []
            #print(f"k is now {k}")
            for mn, pair in sumsindex.items():
                if mn > 0:
                    diff.append(abs(float(k)-mn))
                    temp.append(pair)
            #print(f"the candidate diffs are:")
            #print(diff)
            #print(f"the candidate pairs are:")
            #print(temp)
            minindex = diff.index(min(diff))
            one = M.index(temp[minindex][0]) + 1
            two = N.index(temp[minindex][1]) + 1
            outF.write(f"{one} {two}" + '\n')
            #print(one, two)
outF.close()

print("end")
