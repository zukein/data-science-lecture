import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib_venn import venn2


def show():
    v = venn2((2, 2, 1), set_labels=('', ''))
    v.get_label_by_id('10').set(text='$A$')
    v.get_label_by_id('01').set(text='$B$')
    v.get_label_by_id('11').set(text=r'$A\cap B$')
    ax = plt.gca()
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    width = xmax - xmin
    height = ymax - ymin
    margin = 0.01
    padding = 0.1
    ax.text(xmin + width*padding, ymax - height*padding, '$U$')
    ax.add_patch(Rectangle((xmin + width*margin, ymin + height*margin),
                           width*(1 - margin*2), height*(1 - margin*2),
                           edgecolor='black', fill=False))
    plt.show()
