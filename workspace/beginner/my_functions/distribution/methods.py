import numpy as np
from scipy.stats import norm
from ipywidgets import interact, FloatSlider
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect

x_min, x_max = -3, 3
resolution = 50
xx = np.linspace(x_min, x_max, resolution)


def pdf():
    y = norm.pdf(xx)

    def plot(i):
        o = norm.pdf(i)

        plt.figure(figsize=figaspect(1))
        ax = plt.axes()
        ax.plot(xx, y, color='black')
        ax.vlines(i, o, color='black', linestyles=':')
        ax.hlines(o, x_min, i, color='black', linestyles=':')
        ax.set(ax,
               title='pdf (確率密度関数)',
               xlabel='実数',
               ylabel='確率密度',
               xlim=(x_min, x_max),
               ylim=(0, 0.5),
               xticks=[i],
               yticks=[o],
               xticklabels=['in'],
               yticklabels=['out'])
        ax.get_yticklabels().set(color='blue')
        plt.show()

    interact(plot,
             i=FloatSlider(value=1,
                           min=x_min,
                           max=x_max,
                           step=0.5,
                           description='入力：',
                           continuous_update=False,
                           readout=False))


def plot_pdf_area(ax, x_range, color='blue', area_label='out'):
    ax.plot(xx, norm.pdf(xx), color='black')
    ax.fill_between(x_range,
                    0,
                    norm.pdf(x_range),
                    color=color,
                    label=area_label)
    ax.legend()
    ax.set(title='pdf (確率密度関数)',
           xlabel='実数',
           ylabel='確率密度',
           ylim=(0, 1),
           yticks=())


def plot_cdf(ax, x, y, y_origin=0, color='blue'):
    ax.plot(xx, norm.cdf(xx), color='black')
    ax.vlines(x, 0, y, color='black', linestyles=':')
    ax.hlines(y, x_min, x, color='black', linestyles=':')
    ax.vlines(x_min, y_origin, y, color=color, linewidth=7)
    ax.set(title='cdf (累積分布関数)',
           xlabel='実数',
           ylabel='累積確率',
           xlim=(x_min, x_max),
           ylim=(0, 1),
           xticks=[x],
           yticks=[0, y, 1])


def cdf():
    def plot(i):
        _, (ax1, ax2) = plt.subplots(1,
                                     2,
                                     figsize=figaspect(1 / 2),
                                     sharex=True)
        plot_cdf(ax1, i, norm.cdf(i))
        ax1.set(xticklabels=['in'], yticklabels=[0, 'out', 1])
        plot_pdf_area(ax2, np.linspace(x_min, i, resolution))
        plt.show()

    interact(plot,
             i=FloatSlider(value=1,
                           min=x_min,
                           max=x_max,
                           step=0.5,
                           description='入力：',
                           continuous_update=False,
                           readout=False))


def sf():
    def plot(i):
        _, (ax1, ax2) = plt.subplots(1,
                                     2,
                                     figsize=figaspect(1 / 2),
                                     sharex=True)
        plot_cdf(ax1, i, 1 - norm.sf(i), y_origin=1)
        ax1.set(xticklabels=['in'], yticklabels=[0, '', 1])
        plot_pdf_area(ax2, np.linspace(i, x_max, resolution))
        plt.show()

    interact(plot,
             i=FloatSlider(value=1,
                           min=x_min,
                           max=x_max,
                           step=0.5,
                           description='入力：',
                           continuous_update=False,
                           readout=False))


def ppf():
    def plot(i):
        x = norm.ppf(i)
        _, (ax1, ax2) = plt.subplots(1,
                                     2,
                                     figsize=figaspect(1 / 2),
                                     sharex=True)
        plot_cdf(ax1, x, i, color='darkgray')
        ax1.set(xticklabels=['out'], yticklabels=[0, 'in', 1])
        plot_pdf_area(ax2,
                      np.linspace(x_min, x, resolution),
                      color='darkgray',
                      area_label='in')
        for ax in [ax1, ax2]:
            for ticklabel in ax.get_xticklabels():
                ticklabel.set(color='blue')
        plt.show()

    interact(plot,
             i=FloatSlider(value=0.55,
                           min=0.05,
                           max=0.95,
                           step=0.1,
                           description='入力：',
                           continuous_update=False,
                           readout=False))


def isf():
    def plot(i):
        x = norm.isf(i)
        _, (ax1, ax2) = plt.subplots(1,
                                     2,
                                     figsize=figaspect(1 / 2),
                                     sharex=True)
        plot_cdf(ax1, x, 1 - i, y_origin=1, color='darkgray')
        ax1.set(xticklabels=['out'], yticklabels=[0, 'in', 1])
        plot_pdf_area(ax2,
                      np.linspace(x, x_max, resolution),
                      color='darkgray',
                      area_label='in')
        for ax in [ax1, ax2]:
            for ticklabel in ax.get_xticklabels():
                ticklabel.set(color='blue')
        plt.show()

    interact(plot,
             i=FloatSlider(value=0.55,
                           min=0.05,
                           max=0.95,
                           step=0.1,
                           description='入力：',
                           continuous_update=False,
                           readout=False))
