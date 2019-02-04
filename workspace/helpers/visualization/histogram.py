import matplotlib.pyplot as plt
import seaborn as sns


def show():
    tips = sns.load_dataset('tips')
    sns.distplot(tips['total_bill'], kde=False)
    plt.show()
