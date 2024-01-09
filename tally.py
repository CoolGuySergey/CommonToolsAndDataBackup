# Tallies failing pattern
import pandas as pd
import numpy as np

with open('log.txt') as f:
    lines = f.readlines()
SeqCount = float(lines[2].strip('\n').split()[-1])
InvalidPairs = float(lines[3].strip('\n').split()[-1])
ValidPairs = float(lines[4].strip('\n').split()[-1])
BowAlpha = float(lines[7].strip('\n').split()[2])
StuAlpha = float(lines[10].strip('\n').split()[2])
AbaAlpha = float(lines[13].strip('\n').split()[2])

BowDF = pd.read_csv('AllBowkers.csv', dtype={'a': np.float32}, index_col=0)
StuDF = pd.read_csv('AllStuarts.csv', dtype={'a': np.float32}, index_col=0)
AbaDF = pd.read_csv('AllAbabnehs.csv', dtype={'a': np.float32}, index_col=0)

# >>> BowDF.columns.tolist() == StuDF.columns.tolist()
# True

BowBool = BowDF < BowAlpha
StuBool = StuDF < StuAlpha
AbaBool = AbaDF < AbaAlpha

tally = {
    "B0S0A0": int(0),
    "B0S1A0": int(0),
    "B0S0A1": int(0),
    "B0S1A1": int(0),
    "B1S0A0": int(0),
    "B1S1A0": int(0),
    "B1S0A1": int(0),
    "B1S1A1": int(0),
}

for i in BowBool.index.values.tolist():   # iterate over rows
    for j in BowBool.columns.tolist():    # iterate over columns
        
        BowVal = "B" + str(int(not BowBool.at[i, j]))     # get  value
        StuVal = "S" + str(int(not StuBool.at[i, j]))
        AbaVal = "A" + str(int(not AbaBool.at[i, j]))
        
        Status = str(BowVal + StuVal + AbaVal)
        tally[Status] += 0.5

# NaNs from invalid pairs are tallying into B1S1A1 as "all passing"
# NaNs from main-daig are tallying into B1S1A1 as "all passing"
tally['B1S1A1'] = tally['B1S1A1'] - SeqCount/2 - InvalidPairs

print(tally)
percs = dict(zip(tally.keys(), [x/123638.0*100 for x in tally.values()]))
print(percs)
print(f"total tallied: {sum(tally.values())}")
print([x/123638.0*100 for x in tally.values()])
print(f"total valid pairs: {ValidPairs}")
print(f"All pairs accounted for: {sum(tally.values()) == ValidPairs}")
