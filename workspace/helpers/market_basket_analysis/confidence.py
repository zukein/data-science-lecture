import matplotlib.pyplot as plt
from matplotlib_venn import venn2


def show():
    v = venn2((2, 2, 1), set_labels=('', ''),
              set_colors=('lightgray', 'white'))
    for idx, text in zip(('10', '01'), ('A', 'B')):
        v.get_label_by_id(idx).set(text=text)
        v.get_patch_by_id(idx).set(edgecolor='black')
    v.get_label_by_id('11').set(text=r'$A\cap B$')
    v.get_patch_by_id('11').set(facecolor='blue')
    ax = plt.gca()
    ax.set(title=r'$conf( A\Rightarrow B)=$青/灰')
    plt.show()
