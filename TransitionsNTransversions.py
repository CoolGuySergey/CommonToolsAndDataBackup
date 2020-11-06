# Transition and Transversion
# transitions A <--> G or C <--> T
# transversion all other changes

allseqs = []
with open("exam1.fasta", "r") as input_file:
    alllines = input_file.read().splitlines()
for line in alllines:
    if not line.startswith(">"):
        allseqs = allseqs + [str(line)]

seq1 = allseqs[0]
seq2 = allseqs[1]
sitcount = 0
vercount = 0

for i in range(len(seq1)):
    if seq1[i] != seq2[i]:
        if (seq1[i] == "A" and seq2[i] == "G") or (seq1[i] == "G" and seq2[i] == "A") or (seq1[i] == "C" and seq2[i] == "T") or (seq1[i] == "T" and seq2[i] == "C"):
            sitcount += 1
        else:
            vercount += 1

print(sitcount/vercount)
