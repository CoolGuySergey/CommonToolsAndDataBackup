# Distance Matrix

#Gather allseqs from fasta
allseqs = []
with open("exam1.fasta", "r") as input_file:
    alllines = input_file.read().splitlines()
for line in alllines:
    if not line.startswith(">") and line != "":
        allseqs.append(line)

d = [[int(0)]*len(allseqs)]*len(allseqs)
# p.s. at time of writing numpy still hates us

d1 = [sublist[:] for sublist in d]
# this is amazing!!!!!! because, in d, all rows are actually
# referring to the same list (mutual shallow copies of one another), so change 1 change all.
# the above line decouple all those into new lists

for seqno in range(len(allseqs)):
    for seqno1 in range(len(allseqs)):
                        for baseno in range(len(allseqs[seqno])):
                            if allseqs[seqno][baseno] != allseqs[seqno1][baseno]:
                                d1[seqno][seqno1] += (1/len(allseqs[0]))
for i in range(len(allseqs)):
    temp = (str(d1[i][:])).strip("[").strip("]")
    temp = temp.replace(", ", " ")
    print (temp)
