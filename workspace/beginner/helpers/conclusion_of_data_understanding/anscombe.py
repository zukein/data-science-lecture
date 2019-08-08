import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect


class Anscombe(object):
    def __init__(self):
        anscombe = sns.load_dataset('anscombe')
        levels = [sorted(anscombe['dataset'].unique()), ['x', 'y']]
        codes = np.array([i for i in np.ndindex(*[len(l) for l in levels])]).T
        values = None
        for dataset in levels[0]:
            for var in levels[1]:
                subset = anscombe.loc[anscombe['dataset'] == dataset, var]
                values = np.column_stack([values, subset
                                          ]) if values is not None else subset
        self.data = pd.DataFrame(
            values, columns=pd.MultiIndex(levels=levels, codes=codes))

    def show(self):
        names = self.data.columns.levels[0].tolist()
        _, axes = plt.subplots(
            2, 2, figsize=figaspect(1), sharex=True, sharey=True)
        for i, ax in enumerate(axes.ravel()):
            x = self.data[(names[i], 'x')]
            y = self.data[(names[i], 'y')]
            ax.scatter(x, y)
            ax.set(
                title=names[i],
                xticks=(),
                yticks=(),
                xlabel='$x$' if i > 1 else None)
            ax.set_ylabel(ylabel='$y$' if i % 2 is 0 else None, rotation=0)
        plt.show()
