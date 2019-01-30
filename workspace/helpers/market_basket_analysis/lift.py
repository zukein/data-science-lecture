import matplotlib.pyplot as plt
from matplotlib.figure import figaspect
from matplotlib.patches import Rectangle
from matplotlib_venn import venn2


def set_label(venn):
    for idx, text in zip(('10', '01'), ('A', 'B')):
        venn.get_label_by_id(idx).set(text=text)
        venn.get_patch_by_id(idx).set(edgecolor='black')
    venn.get_label_by_id('11').set(text=r'$A\cap B$')


def show():
    _, (ax1, ax2) = plt.subplots(
        1, 2, figsize=figaspect(1/3), sharex=True, sharey=True)

    v1 = venn2((2, 2, 1), set_labels=('', ''),
               set_colors=('lightgray', 'white'), ax=ax1)
    set_label(v1)
    v1.get_patch_by_id('11').set(facecolor='blue')
    ax1.set(title=r'分子$=conf( A\Rightarrow B)$')

    v2 = venn2((2, 2, 1), set_labels=('', ''),
               set_colors=('lightgray', 'blue'), ax=ax2)
    set_label(v2)
    v2.get_patch_by_id('11').set(facecolor='blue')
    ax2.set(title='分母$=supp( B)$')
    xmin, xmax = ax2.get_xlim()
    ymin, ymax = ax2.get_ylim()
    width = xmax - xmin
    height = ymax - ymin
    margin = 0.01
    padding = 0.1
    ax2.text(xmin + width*padding, ymax - height*padding, '$N$')
    ax2.add_patch(Rectangle((xmin + width*margin, ymin + height*margin),
                            width*(1 - margin*2), height*(1 - margin*2),
                            facecolor='lightgray', zorder=0))

    plt.show()
