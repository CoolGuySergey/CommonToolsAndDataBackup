# Given mRNA, scan for all possible Open Reading Frames
# There are six scans we have to do
# DNA and DNArev, with wrapping1,2,3

# Generating both for and rev strands

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

DNA = str(open("exam1.fasta", "r").read().splitlines())
DNA=DNA.strip("['").strip("']")

DNArev = DNA.replace("C", "g").replace("G", "c").replace("T", "a").replace("A", "t")
DNArev = DNArev[::-1].upper()

# Trying all three codon reading frames
# Gathering all six full-translations
from textwrap import wrap
DNA1 = wrap(DNA, 3)
DNA2 = wrap(DNA[1:-2], 3)
DNA3 = wrap(DNA[2:-1], 3)
DNArev1 = wrap(DNArev, 3)
DNArev2 = wrap(DNArev[1:-2], 3)
DNArev3 = wrap(DNArev[2:-1], 3)

allPeptides = [translate(DNA1)] + [translate(DNA2)] + [translate(DNA3)] + [translate(DNArev1)] + [translate(DNArev2)] + [translate(DNArev3)]

# From six full-translations, take all possible ORFs
# str.find("M") will only return the position of first M
# This will give us all positions where there is M
def find_all(master, sub):
    start = 0
    while True:
        start = master.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)
        # Use as part of list as with example below

Orfs = []
for searchbase in allPeptides:
    # iterate through six complete translations
    for startpos in list(find_all(searchbase, 'M')):
        # iterate through all M-starts
        if (searchbase[startpos:].find("_")) != -1:
            # discard all that starts with M but has no stop
            Orfs = Orfs + [((searchbase[startpos:]).split("_"))[0]]
            # split by "_": if the whole thing starts with M
            # and we split the whole thing by "_", we only want
            # the first element
            
final = list(dict.fromkeys(Orfs))
print(*final, sep='\n')
# collapse duplicates in list, convert to dict then back to list

