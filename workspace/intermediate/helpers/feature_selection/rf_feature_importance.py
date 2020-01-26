import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect


def show():
    loader = load_breast_cancer()
    X, y = loader.data, loader.target

    model = RandomForestClassifier(n_estimators=1000,
                                   random_state=1234,
                                   n_jobs=-1)
    model.fit(X, y)

    features = loader.feature_names
    n_feature = len(features)
    importances = model.feature_importances_
    indices = np.argsort(importances)[::-1]

    fig = plt.figure(figsize=figaspect(10 / n_feature))
    ax = fig.gca()

    ax.bar(np.arange(n_feature), importances[indices], align='center')
    ax.set(title='特徴の重要度', xlim=(-1, n_feature))
    ax.xaxis.set(ticks=np.arange(n_feature), ticklabels=features[indices])
    for ticklabel in ax.xaxis.get_majorticklabels():
        ticklabel.set(rotation=90, size='large')

    plt.show()
