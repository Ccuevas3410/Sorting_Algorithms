import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


import Algorithms as algo







ix3 = pd.MultiIndex.from_arrays([
      ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b'],
    ['foo', 'foo', 'bar', 'bar', 'foo', 'foo', 'bar', 'bar']], names=['letter', 'word'])
df3 = pd.DataFrame({'data1': [3, 2, 4, 3, 2, 4, 3, 2],'data2': [6, 5, 7, 5, 4, 5, 6, 5]}, index=ix3)

gp3 = df3.groupby(level=('letter', 'word'))
means = gp3.mean()
errors = gp3.std()
means

fig, ax = plt.subplots()
means.plot.bar(yerr=errors, ax=ax, capsize=4)