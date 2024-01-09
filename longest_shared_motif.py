# Longest shared motif

#Gather allseqs from fasta
allseqs = []
with open("exam1.fasta", "r") as input_file:
    alllines = input_file.read().splitlines()
for line in alllines:
    if not line.startswith(">") and line != "":
        allseqs.append(line)
    
# shortest length: scan for if its full is repeated
# then scan for all its len-1 substrings, len-2
# substrings, all the way to len-(len-2) substrings
targetseq = min(allseqs, key=len)
setseqs = set(allseqs) - set(targetseq)
allseqs = list(setseqs)

shared_motifs = []
for i in range(len(targetseq)+1):
    for j in reversed(range(i+2, (len(targetseq)+1))):
        #print(targetseq[i:j])
        #print(f"above is {i}th through to {j}th") #loop through all substrings

        minitarget = targetseq[i:j] #we have to look for this in ALL other sequences
        minitargetpass = 0 #reset to 0 with every new minitarget
        
        for seq in allseqs: 
            if minitarget in seq:
                minitargetpass += 1
                if minitargetpass == len(allseqs): #want the minitarget that can max pass
                    shared_motifs = shared_motifs + [minitarget]
            else: #if not in one seq, give up the loop entirely
                break              
print(max(shared_motifs, key=len))
