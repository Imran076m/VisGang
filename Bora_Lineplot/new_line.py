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
import Bora_Final_Data as ed

saveValue = -1


df_recent = pd.DataFrame()

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id="graph"),
    dcc.Dropdown(
        id="dropdown",
        options=[
            {"label": "Entire United Kingdom", "value": 0},
            {"label": "London", "value": 1},
            {"label": "Cumbria", "value": 3},
            {"label": "Lancashire", "value": 4},
            {"label": "Merseyside", "value": 5},
            {"label": "Great Manchester", "value": 6},
            {"label": "Cheshire", "value": 7},
            {"label": "Northumbria", "value": 10},
            {"label": "Durham", "value": 11},
            {"label": "North Yorkshire", "value": 12},
            {"label": "West Yorkshire", "value": 13},
            {"label": "South Yorkshire", "value": 14},
            {"label": "Humberside", "value": 16},
            {"label": "Cleveland", "value": 17},
            {"label": "West Midlands", "value": 20},
            {"label": "Staffordshire", "value": 21},
            {"label": "West Mercia", "value": 22},
            {"label": "Warwickshire", "value": 23},
            {"label": "Derbyshire", "value": 30},
            {"label": "Nottinghamshire", "value": 31},
            {"label": "Lincolnshire", "value": 32},
            {"label": "Leicestershire", "value": 33},
            {"label": "Northamptonshire", "value": 34},
            {"label": "Cambridgeshire", "value": 35},
            {"label": "Norfolk", "value": 36},
            {"label": "Suffolk", "value": 37},
            {"label": "Bedfordshire", "value": 40},
            {"label": "Hertfordshire", "value": 41},
            {"label": "Essex", "value": 42},
            {"label": "Thames Valley", "value": 43},
            {"label": "Hampshire", "value": 44},
            {"label": "Surrey", "value": 45},
            {"label": "Kent", "value": 46},
            {"label": "Sussex", "value": 47},
            {"label": "City of London", "value": 48},
            {"label": "Devon and Cornwall", "value": 50},
            {"label": "Avon and Somerset", "value": 52},
            {"label": "Gloucestershire", "value": 53},
            {"label": "Wiltshire", "value": 54},
            {"label": "Dorset", "value": 55},
            {"label": "North Wales", "value": 60},
            {"label": "Gwent", "value": 61},
            {"label": "South Wales", "value": 62},
            {"label": "Dyfed-Powys", "value": 63},
            {"label": "Northern Scotland", "value": 91},
            {"label": "Grampian", "value": 92},
            {"label": "Tayside", "value": 93},
            {"label": "Fife", "value": 94},
            {"label": "Lothian and Borders", "value": 95},
            {"label": "Central Scotland", "value": 96},
            {"label": "Strathclyde", "value": 97},
            {"label": "Dumfries and Galloway", "value": 98},
            ],
        value=0,
        clearable=False,
    )
])


@app.callback(
    Output("graph", "figure"), 
    [Input("dropdown", "value")])
def update_line_chart(value):
    global df_recent
    global saveValue
    index = value
    
    if saveValue == -1:
        saveValue = index
        df_final = ed.createDFrame(index)
        df_recent = df_final
        
    else:
        if saveValue == index:
          df_final = df_recent
        else:
          saveValue = index
          df_final = ed.createDFrame(index)
          df_recent = df_final
          
    #x, y = 'year', 'total_accident'
    
    fig = px.line(df_final, x='year', y='total_accident', title="Total Number of Accidents Throughout The Years",
                  labels=dict(total_accident="Total Number of Accidents", year="Year"), markers=True)
    fig.update(layout_yaxis_range = [0,300000])    
    return fig


if __name__ == "__main__":
    app.run_server(debug=False, dev_tools_ui=False)
