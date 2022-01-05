# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 18:25:12 2021

@author: 20201349
"""


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv("accident_2005-2011.csv")


app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id="graph"),
    html.Button("Switch Axis", id='btn', n_clicks=0)
])


@app.callback(
    Output("graph", "figure"), 
    [Input("btn",'n_clicks')])
def display_graph(n_clicks):
    if n_clicks % 2 == 0:
        x, y = 'year', 'total_accident'
    else:
        x,y = 'year', 'mean_casualty'
    
    fig = px.line(df, x=x, y=y)    
    return fig


if __name__ == "__main__":
    app.run_server(debug=False, dev_tools_ui=False)
