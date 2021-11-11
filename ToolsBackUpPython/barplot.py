import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame(
    columns=["Behaviour Tally",
             "Codon 1",
             "Codon 2",
             "Codon 3",
             "Unpartitioned",
    ],
    data=[
        ['B0S0A0', 28, 0, 919, 2815],
        ['B0S1A0', 37, 0, 272, 495],
        ['B0S0A1', 49210, 13640, 70333, 76555],
        ['B0S1A1', 1227, 298, 1220, 1946],
        ['B1S0A0', 0, 0, 0, 0],
        ['B1S1A0', 4, 0, 18, 19],
        ['B1S0A1', 3710, 2875, 3256, 2260],
        ['B1S1A1', 69422, 106815, 47620, 39550],
    ]
)

#sns.set()
#df.set_index("Behaviour Tally").T.plot(kind="bar", stacked=True)
#plt.show()

from matplotlib.colors import ListedColormap

df.set_index("Behaviour Tally")\
  .reindex(df.set_index("Behaviour Tally").sum().sort_values().index, axis=1)\
  .T.plot(kind='bar',
          stacked=True,
          colormap=ListedColormap(sns.color_palette("GnBu", 8)), 
          figsize=(12,6))

plt.show()
