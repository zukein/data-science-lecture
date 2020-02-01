import numpy as np
from scipy.linalg import eigh
import pandas as pd
import plotly.express as px

n = 100

np.random.seed(1234)


def show():
    df = pd.DataFrame()

    for r in range(-10, 11):
        r /= 10
        mat = np.array([[1.0, r], [r, 1.0]])
        a = np.random.normal(size=(2, n))
        evals, evecs = eigh(mat)
        c = evecs.dot(np.diag(np.sqrt(evals)))
        x, y = c.dot(a)

        df = df.append(pd.DataFrame({'x': x, 'y': y, '相関係数': r}))

    fig = px.scatter(df,
                     'x',
                     'y',
                     animation_frame='相関係数',
                     width=600,
                     height=600)
    fig.show()
