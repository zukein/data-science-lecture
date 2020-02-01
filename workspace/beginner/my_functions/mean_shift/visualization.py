import numpy as np
from sklearn.cluster import MeanShift
from ipywidgets import interact, FloatSlider, fixed
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect
from matplotlib.patches import Circle, Patch
import seaborn as sns

resolution = 200


def plot(bandwidth, df):
    x = df.values
    model = MeanShift(bandwidth=bandwidth, n_jobs=-1)
    model.fit(x)
    plt.figure(figsize=figaspect(1))
    ax = plt.axes()
    ax.set(aspect='equal')
    df.plot.scatter(df.columns[0], df.columns[1], c='black', s=10, ax=ax)
    xlim, ylim = ax.get_xlim(), ax.get_ylim()
    side = max(xlim[1] - xlim[0], ylim[1] - ylim[0])
    x_center, y_center = sum(xlim) / 2, sum(ylim) / 2
    xx, yy = np.meshgrid(
        np.linspace(x_center - side / 2, x_center + side / 2, resolution),
        np.linspace(y_center - side / 2, y_center + side / 2, resolution))
    grid = np.c_[xx.ravel(), yy.ravel()]
    pred = model.predict(grid)
    palette = sns.color_palette()
    ax.scatter(
        xx,
        yy,
        c=[palette[i] for i in pred],
        marker='.',
        alpha=0.2,
        edgecolors='none')
    centers = model.cluster_centers_
    ax.scatter(
        centers[:, 0],
        centers[:, 1],
        marker='x',
        s=100,
        c='blue',
        label='クラスタ中心')
    for center in centers:
        ax.add_patch(
            Circle(
                xy=center,
                radius=bandwidth,
                fill=False,
                edgecolor='black',
                linestyle='--'))
    handles, labels = ax.get_legend_handles_labels()
    handles.extend([Patch(color=palette[i]) for i in range(len(centers))])
    labels.extend([f'クラスタ{i + 1}' for i in range(len(centers))])
    ax.legend(handles, labels)
    ax.set(
        xlim=(xx.min(), xx.max()),
        ylim=(yy.min(), yy.max()),
        xticks=(),
        yticks=())
    plt.show()


def show(df):
    bandwidth = FloatSlider(
        value=0.5,
        min=0.3,
        max=0.9,
        step=0.1,
        description='距離',
        readout_format='.1f',
        continuous_update=False)
    interact(plot, bandwidth=bandwidth, df=fixed(df))
