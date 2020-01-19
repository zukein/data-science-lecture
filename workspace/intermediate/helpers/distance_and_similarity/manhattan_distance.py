import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect


def show():
    points = np.array([[1, 1], [2, 2]])
    fig = plt.figure(figsize=figaspect(1))
    ax = fig.gca()
    ax.axhline(0, color='black', alpha=0.2)
    ax.axvline(0, color='black', alpha=0.2)

    def scatter_with_annotation(ax, text, point):
        ax.scatter(*point, color='gray')
        ax.text(point[0], point[1] + 0.1, text, horizontalalignment='right')

    scatter_with_annotation(ax, 'A', points[0])
    scatter_with_annotation(ax, 'B', points[1])
    ax.annotate(None,
                points[0],
                xytext=points[1],
                arrowprops=dict(
                    arrowstyle="-",
                    color="red",
                    alpha=0.4,
                    connectionstyle="angle, angleA = 90, angleB = 0"))
    ax.text(points[1, 0],
            points[0, 1],
            'd',
            size='large',
            color='red',
            horizontalalignment='left',
            verticalalignment='top')
    ax.set(xlim=(-0.5, 3), ylim=(-0.5, 3), xticks=(0, ), yticks=(0, ))
    plt.show()