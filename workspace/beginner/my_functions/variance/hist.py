import numpy as np
import pandas as pd
import plotly.express as px

np.random.seed(1234)


def show():
    df = pd.DataFrame()

    for scale in range(5, 21):
        scale /= 10
        x = np.random.normal(size=40000, scale=scale)
        df = df.append(pd.DataFrame({'データの散らばり具合': scale, 'x': x}))

    fig = px.histogram(df,
                       'x',
                       animation_frame='データの散らばり具合',
                       labels={'x': ''},
                       histnorm='probability density',
                       range_x=(-6, 6),
                       range_y=(0, 1),
                       nbins=200,
                       width=600,
                       height=600)
    fig.show()
