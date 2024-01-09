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
        ['Marginal and Internal Symmetries breaking Global Symmetry', 28, 0, 919, 2815],
        ['Internal Symmetry breaking Global Symmetry', 37, 0, 272, 495],
        ['Marginal Symmetry breaking Global Symmetry', 49210, 13640, 70333, 76555],
        ['Marginal, Internal, Global Symmetries maintained', 69422, 106815, 47620, 39550],
    ]
)

from matplotlib.colors import ListedColormap

ax = df.set_index("Behaviour Tally")\
  .reindex(df.set_index("Behaviour Tally").sum().index, axis=1)\
  .T.plot(kind='bar',
          stacked=True,
          colormap=ListedColormap(sns.color_palette("hls", 4))
  )

# Put the legend out of the figure
plt.legend(bbox_to_anchor=(0, 1, 1, 0.2),
           loc="lower left", borderaxespad=0.)
# Turn tick labels
plt.setp(ax.get_xticklabels(), rotation=0)
plt.show()
