import dash
from dash import dcc
from dash import html
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
from accidentdata import Accidents
import plotly.graph_objects as go


app = dash.Dash(__name__)

#fig_map = Accidents.outMap()


app.layout = html.Div([
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
    ),
    dcc.Graph(id="bar-chart"),
    dcc.Graph(id="pie-chart"),
    dcc.Graph(id="line-chart")
])

@app.callback(
    Output("bar-chart", "figure"), 
    [Input("dropdown", "value")])
def update_bar(value):
    index = value
    df_bar = Accidents.outFrameBar(index)
       
    fig = fig = px.bar(df_bar, y=df_bar.index.get_level_values(0), 
                       x="count",
                       color= df_bar.index.get_level_values(1),
                       barmode = 'stack',
                       orientation = "h",
                       range_x = [0, 800000]
                       )
    
    fig.update_layout(
        yaxis={'categoryorder':'array', 'categoryarray':['post-EC','EC','pre-EC']},
        xaxis_title = "Number of Fatal Casualties",
        yaxis_title = "Time Era",
        title = "Fatal Casualties Before, During and After the Economic Crisis"
        )
    
    return fig

@app.callback(
    Output("pie-chart", "figure"), 
    [Input("dropdown", "value")])
def update_pie(value):
    index = value
    df_pie = Accidents.outPie(index)
    
    fig = px.sunburst(df_pie, path=['Accident year', 'Injury'], 
                  values='Count', color="Accident year",
                  hover_name = 'Accident year',
                  title = 'Sum of Casualties by Age Range',
                  )

    fig.update_traces(
        go.Sunburst(hovertemplate='%{customdata[0]}<br> Sum:%{value:,.0f}'),
        insidetextorientation='radial')


     
    return fig

@app.callback(
    Output("line-chart", "figure"), 
    [Input("dropdown", "value")])
def update_line_chart(value):
    index = value
    df_line = Accidents.outLine(index)
    
    fig = px.line(df_line, x='year', y='total_accident', title="Total Number of Accidents Throughout The Years",
                  labels=dict(total_accident="Total Number of Accidents", year="Year"), markers=True)
    fig.update(layout_yaxis_range = [0,300000])    
    return fig
    
app.run_server(debug=False, dev_tools_ui=False)