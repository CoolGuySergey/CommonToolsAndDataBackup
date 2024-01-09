# RNA Splicing

def translate(seq):
    codontable = { 
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                  
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W', 
    }
    
    protein = ""
    for i in seq:
        if len(i) == 3:
            aa = codontable[i]
            protein += aa
    return (protein)


# Gathering introns here
allintrons = []  
with open("exam.fasta", "r") as input_file:
    alllines = input_file.read().splitlines()

for line in alllines:
    if not line.startswith(">"):
        print(line)
        allintrons = allintrons + [str(line)]

    # Splicing out introns from DNA

DNA = "ATGAGGACTCTACACAGTTCACATCGCG"
for i in allintrons:
    DNA = DNA.replace(i, "")
    # Translating extrons

from textwrap import wrap
seq = wrap(DNA, 3)
translate(seq)
