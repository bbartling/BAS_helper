import random
import numpy as np
import pandas as pd

import chart_studio.plotly as py
import plotly.graph_objs as go

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate


df = pd.read_csv('./TOU_rates_kwh_summer.csv', index_col='hour')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

xs=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

trace1 = go.Bar(
    x=xs,
    y=df.dollar.tolist(),
    name='$/kWh TOU Rates'
)
trace2 = go.Scatter(
    x=xs,
    y=[random.randint(0, 100) for x in range(24)],
    name='$ Projected Costs',
    yaxis='y2'
)



app.layout = html.Div(children=[
    html.H1(children='Electricity Time of Use and Cooling Load Forecast Costs', id='first'),
    #dcc.Interval(id='timer', interval=1000),
    html.Div(id='dummy'),
    dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    trace1, trace2,
                ],
                'layout': go.Layout(
                title='Daily Projected Costs',
                xaxis=dict(
                    title='Hour In Day'
                ),
                yaxis=dict(
                    title='Utility TOU Rates - $/kWh'
                ),
                yaxis2=dict(
                    title='Dollars - $',
                    titlefont=dict(
                        color='rgb(148, 103, 189)'
                    ),
                    tickfont=dict(
                        color='rgb(148, 103, 189)'
                    ),
                    overlaying='y',
                    side='right'
                )
            )
        }
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)
