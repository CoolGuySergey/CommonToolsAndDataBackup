# Consensus and Profile
# A profile is a democratic count of bases at all locations
# We then take the consensus based on that

# e.g. Consensus is ATGCAACT
# A: 5 1 0 0 5 5 0 0
# C: 0 0 1 4 2 0 6 1
# G: 1 1 6 3 0 1 0 0
# T: 1 5 0 0 0 1 1 6

# Gather sequences
allseqs = []
with open("test.fasta", "r") as input_file:
    alllines = input_file.read().splitlines()
for line in alllines:
    if not line.startswith(">"):
        allseqs = allseqs + [str(line)]

# Make empty matrix for profile
d = [[int(0)]*len(allseqs[0]),
     [int(0)]*len(allseqs[0]),
     [int(0)]*len(allseqs[0]),
     [int(0)]*len(allseqs[0])]
     # four nucleotide rows, as many columns as first seq is long
     # numpy hates us at time of writing. Beware of shallow copying if just use *4

# Collect base calls
for seq in allseqs:
    for i in range(len(seq)):
        if seq[i] == "A":
           #print(f"I got an A in position{i}!")
            d[0][i] += 1
        elif seq[i] == "C":
            #print(f"I got an C in position{i}!")
            d[1][i] += 1
        elif seq[i] == "G":
            #print(f"I got an G in position{i}!")
            d[2][i] += 1
        else:
            #print(f"I got an T in position{i}!")
            d[3][i] += 1
                            
# Create consensus
cons = ""
for i in range(len(d[0])):
    all_calls = list(str(d[0][i]) + str(d[1][i])+ str(d[2][i]) + str(d[3][i]))
    all_bases = ["A", "C", "G", "T"]
    tempdict = dict(zip(all_bases, all_calls))
    cons = cons + (max(tempdict, key=tempdict.get))
    del tempdict

# Much shorter with lambda:

strands = [x.strip() for x in f.readlines()]

matrix = zip(*strands)

profile_matrix = map(lambda x: dict((base, x.count(base)) for base in "ACGT"), matrix)

consensus = [max(x,key = x.get) for x in profile_matrix]

print "".join(consensus);

for base in "ACGT":
    print base+":",
    for x in profile_matrix:
        print x[base],
    print ""
