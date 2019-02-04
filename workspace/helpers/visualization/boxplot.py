import matplotlib.pyplot as plt
import seaborn as sns


def show():
    sns.load_dataset('iris').boxplot('sepal_width')
    plt.show()
