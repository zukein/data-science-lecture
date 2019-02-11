from scipy import stats
from ipywidgets import interact, FloatRangeSlider
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect

xrange = (-5.0, 10.0)
xlim = (-6.0, 11.0)


def plot(float_range):
    x_min, x_max = float_range
    p = stats.uniform.pdf(float_range, loc=x_min, scale=x_max - x_min)
    plt.figure(figsize=figaspect(1))
    ax = plt.axes()
    ax.fill_between(float_range, p)
    ax.set(
        title='一様分布',
        xlabel=f'取りうる値 ({float_range[0]}~{float_range[1]})',
        xlim=xlim,
        xticks=float_range,
        ylim=(0, 1.1))
    ax.set_ylabel('確率密度', rotation=0, horizontalalignment='right')
    plt.show()


def show():
    step = 0.1
    float_range = FloatRangeSlider(
        value=[0, 5.0],
        min=xrange[0],
        max=xrange[1],
        step=step,
        description='事象の範囲：',
        continuous_update=False,
        readout_format='.1f')

    def enforce_gap(change):
        new_min, new_max = change.new
        old_min, old_max = change.old
        if new_max - new_min < step:
            if old_min == new_min:
                new_max = new_min + step
            else:
                new_min = new_max - step
            float_range.value = (new_min, new_max)

    float_range.observe(enforce_gap, 'value')
    interact(plot, float_range=float_range)
