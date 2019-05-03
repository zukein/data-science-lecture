import matplotlib.pyplot as plt
import seaborn as sns


def show():
    tips = sns.load_dataset('tips')
    ax = sns.barplot(x='day', y='total_bill',
                     data=tips.groupby('day').sum().reset_index())
    ax.set(title='曜日別売り上げ')
    plt.show()
