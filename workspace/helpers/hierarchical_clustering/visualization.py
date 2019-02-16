from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt


def show(x, labels):
    link = linkage(x, 'ward')
    dendrogram(
        link, labels=labels, leaf_rotation='vertical', leaf_font_size=11)
    fig = plt.gcf()
    height = fig.get_figheight()
    width = fig.get_figwidth()
    fig.set(size_inches=(width * 1.5, height * 1.5))
    plt.show()
