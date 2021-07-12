# GC count for all sequences. Return max score.

def GCcount(seq):
    score = (seq.count("G") + seq.count("C"))/len(seq)*100
    return (score)

allseqs = list()
allscores = list()

    # Fix fasta wrapping in bash so that lines are easy to deal with and not broken
    # Build two empty lists, make dictionary later

with open("exam.fasta", "r") as input_file:
    alllines = input_file.read().splitlines()
    
    # split.lines() instead of just input_file.readlines avoides adding random "/n"s
    
    for line in alllines:
        if line.startswith(">"):
            allseqs.append(line)
        else:
            allscores.append(GCcount(line))

dictionary = dict(zip(allseqs, allscores))

targetscore = max(dictionary.values())

for seq, score in dictionary.items():
    if score == targetscore:
        print (seq)
        print (targetscore)
