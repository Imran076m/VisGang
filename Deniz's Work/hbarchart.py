import dash
from dash import dcc
from dash import html
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
from accidentdata import Accidents
'''
df_acc_pre = pd.read_csv("C:/Users/deniz/Desktop/TUe/Year 2/Q2/JBI100 - Visualisations/Databases/Accidents-2005-2006.csv", low_memory = False)
df_acc_on = pd.read_csv("C:/Users/deniz/Desktop/TUe/Year 2/Q2/JBI100 - Visualisations/Databases/Accidents-2007-2008.csv", low_memory = False)
df_acc_post = pd.read_csv("C:/Users/deniz/Desktop/TUe/Year 2/Q2/JBI100 - Visualisations/Databases/Accidents-2010-2011.csv", low_memory = False)
    
    
df_acc_london_on = df_acc_pre[(df_acc_pre['police_force'] == 1) | (df_acc_pre['police_force'] == 48)]
count_acc_london_on = len(df_acc_london_on[df_acc_london_on['accident_severity'] == 1].value_counts())
count_acc_all_on = len(df_acc_on[df_acc_on['accident_severity'] == 1].value_counts())
    
df_fatal_acc_EC = pd.DataFrame(np.array([count_acc_london_on]), columns = ['Count'])
df_fatal_acc_EC = df_fatal_acc_EC.set_axis(['London'], axis = 0)
df_fatal_acc_EC['Region'] = ['London']
'''
saveValue = -1

df = px.data.tips()
days = df.day.unique()

df_recent = pd.DataFrame()

app = dash.Dash(__name__)


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
])

@app.callback(
    Output("bar-chart", "figure"), 
    [Input("dropdown", "value")])
def update_bar(value):
    global df_recent
    global saveValue
    index = value
    
    if saveValue == -1:
        saveValue = index
        df_final = Accidents.outFrameBar(index)
        df_recent = df_final
        
    else:
        if saveValue == index:
          df_final = df_recent
        else:
          saveValue = index
          df_final = Accidents.outFrameBar(index)
          df_recent = df_final
       
    fig = px.bar(df_final, x = "Count", y = "Time", orientation = "h", range_x = [0, 6000])
    return fig
    
app.run_server(debug=False, dev_tools_ui=False)