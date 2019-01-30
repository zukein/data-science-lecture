import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib_venn import venn2


def show():
    v = venn2((2, 2, 1), set_labels=('', ''),
              set_colors=('lightgray', 'lightgray'))
    for idx, text in zip(('10', '01'), ('A', 'B')):
        v.get_label_by_id(idx).set(text=text)
        v.get_patch_by_id(idx).set(edgecolor='black')
    v.get_label_by_id('11').set(text=r'$A\cap B$')
    v.get_patch_by_id('11').set(facecolor='blue')
    ax = plt.gca()
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    width = xmax - xmin
    height = ymax - ymin
    margin = 0.01
    padding = 0.1
    ax.text(xmin + width*padding, ymax - height*padding, '$N$')
    ax.add_patch(Rectangle((xmin + width*margin, ymin + height*margin),
                           width*(1 - margin*2), height*(1 - margin*2),
                           facecolor='lightgray', zorder=0))
    ax.set(title=r'$supp( A\Rightarrow B)=$青/灰')
    plt.show()
