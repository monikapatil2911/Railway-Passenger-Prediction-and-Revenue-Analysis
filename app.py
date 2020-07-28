from flask import Flask, render_template
import plotly
import plotly.graph_objs as go

import pandas as pd
import numpy as np
# import json
import io  # got moved to io in python3.
import requests

r = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vQ5iMe4q7srLIAow58hokKe8Zv6z5u2hCVDk191Vbt-Mp8i7N2dq3oaIiSfQUFOAfH-Z1nvPwyh3G0r/pub?output=csv')
data = r.content
virar = pd.read_csv(io.BytesIO(data), index_col = 0)
r1 = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vTeERMAFxcU71iZiKV2pScY1rK8OaljkAZ7boH69021Ku63CyzDqevDgTNXS32IkNrI7pkMy4v8Q3Tp/pub?output=csv')
data1 = r1.content
dadar = pd.read_csv(io.BytesIO(data1), index_col = 0)
r2 = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vQVwRNyaJ0Q6bpI1y7LTjLUmquz48MTrt03Y-ZDxmt-ed2BLeplW7HpGpdz22efudSaVexW9ajUiwxv/pub?output=csv')
data2 = r2.content
borivali = pd.read_csv(io.BytesIO(data2), index_col = 0)
r3 = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vRUT8HL1XEe4EYAjKbuKivvIrrUMd-kkn5mlgGPXrq1AtATs7Y-cu_BrucTIYS6p_tRsQd8XTzfV5r9/pub?output=csv')
data3 = r3.content
palghar = pd.read_csv(io.BytesIO(data3), index_col = 0)
r4 = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vRTUOWGhlLILpC93KKe86qiZhkamJ8h-9CVWhCbtc1iz7lYU-EZYx6bjKrUjsjC-iatW1j57SzZOCYc/pub?output=csv')
data4 = r4.content
vasai = pd.read_csv(io.BytesIO(data4), index_col = 0)

y=[len(virar),len(dadar),len(vasai),len(borivali),len(palghar)]
x=['virar','dadar','vasai','borivali','palghar']
x,y
 
app = Flask(__name__)

@app.route('/')

def create_plot():

    fig = go.Figure([go.Bar(x=x, y=y)])
    fig.update_layout(
        title=go.layout.Title(
            text="Total passengers travelled from station till date",
            xref="paper",
            x=0
        ),
        xaxis=go.layout.XAxis(
            title=go.layout.xaxis.Title(
                text="Stations",
                font=dict(
                    family="Oswald",
                    size=18,
                    color="#ff5733"
                )
            )
        ),
        yaxis=go.layout.YAxis(
            title=go.layout.yaxis.Title(
                text="No of passengers",
                font=dict(
                    family="Oswald",
                    size=18,
                    color="#ff5733"
                )
            )
        )
    )

    fig.show()

    # N = 40
    # x = np.linspace(0, 1, N)
    # y = np.random.randn(N)
    # df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe


    # data = [
    #     go.Bar(
    #         x=df['x'], # assign x as the dataframe column 'x'
    #         y=df['y']
    #     )
    # ]
    bar = fig.show()

    # graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('index.html', plot=bar)

# def index():

#     bar = create_plot()
#     return render_template('index.html', plot=bar)

if __name__ == '__main__':
    app.run()