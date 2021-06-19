# Qualification round: Diagnosis

outF = open("output.txt", "w")
outlog = open("log.txt", "w")

# Ingestion
with open("1.txt", "r") as input_file:
    alllines = input_file.read().splitlines()

from treelib import *
from itertools import product
def lca(nodes):
    """Returns the Least Common Ancestor (LCA) of a list of nodes"""
    node1, node2 = nodes
    set1 = set([node1])
    set2 = set([node2])
    while True:
        if node1 in set2:
            return node1
        if node2 in set1:
            return node2
        if tree.parent(node1) is not None:
            node1 = tree.parent(node1).identifier
        if tree.parent(node2) is not None:
            node2 = tree.parent(node2).identifier
        set1.add(node1)
        set2.add(node2)
    else:
        raise Exception("No nodes given")

# Get content of tree
n = alllines[0]
VerticesIndices = [i for i in range(1, int(n)+1)]
VerticesValues = (alllines[2]).split(' ')
DictForTreeVals = dict(zip(VerticesIndices, VerticesValues))

# Build tree
ParentIdentifiers = (alllines[1]).split(' ')
tree = Tree()
tree.create_node("1","1")
for i in range(2, int(n)+1):
    tree.create_node(str(i), str(i), parent=str(ParentIdentifiers[i-2]))
    #tree.show()

# Diseases Info
m = alllines[3]
Diseases = []
for line in alllines[4:4+int(m)]:
    line = line.split(' ')
    line.pop(0)
    Diseases.append(line)

# Patients Info
nq = alllines[4+int(m)]
Patients = []
for line in alllines[-(int(nq)):]:
    line = line.split(' ')
    line.pop(0)
    Patients.append(line)

count=1
for p in Patients:
    scores = []
    for d in Diseases:
        alllcas = [lca([x,y]) for x, y in product(p, d)]
        #print(alllcas)

        temp=0
        for i in alllcas:
            temp += int(DictForTreeVals[int(i)])
        #print (temp)
        scores.append(temp)
        outlog.write(f"End of disease cycle {len(scores)} out of {m}."+'\n')
        outlog.write(f"Current patient cycle {count} out of {nq}" + '\n')
    count+=1
    final = scores.index(max(scores))+1
    outF.write(f"{final}" + '\n')

outlog.write("end")
outF.close()
outlog.close()
