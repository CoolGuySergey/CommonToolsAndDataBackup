# Inferring mRNA from Protein
# Given: A protein string of length at most 1000 aa.
# Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000 (take account of stop codons)

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

# ans must be modulo 10^6, large integers, prevent integer overflows.

all_aas = list(dict.fromkeys(codontable.values()))
# ^just getting a list of al 21 unique aas...
all_combos = []
for aa in all_aas:
    combo = (list(codontable.values())).count(aa)
    all_combos = all_combos + [combo]
aa_combos = dict(zip(all_aas, all_combos))

# The above is prep, use aa_combos to solve prob
with open("exam.fasta", "r") as input_file:
    seq = str(input_file.read().splitlines())
    seq = (seq.strip("']")).strip("['")

poss_combos = 1
for i in seq:
    #print(f"the aa {i} has {aa_combos[i]} possibe codons")
    poss_combos = poss_combos * aa_combos[i]

print(poss_combos % 1000000)
