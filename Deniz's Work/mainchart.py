import dash
from dash import dcc
from dash import html
import plotly.express as px
from dash.dependencies import Input, Output
from accidentdata import Accidents
import plotly.graph_objects as go
import dash_bootstrap_components as dbc


#Initializes the dash app
app = dash.Dash(__name__, 
external_stylesheets=[dbc.themes.SUPERHERO])

#Layout for the dash app
app.layout = html.Div([
    
   #Row for the dropdowns 
   dbc.Row([dbc.Col(dcc.Dropdown(id="dropdown-year",
        options=[
            {"label": "2004", "value": 2004},
            {"label": "2005", "value": 2005},
            {"label": "2006", "value": 2006},
            {"label": "2007", "value": 2007},
            {"label": "2008", "value": 2008},
            {"label": "2009", "value": 2009},
            {"label": "2010", "value": 2010},
            {"label": "2011", "value": 2011},
            {"label": "2012", "value": 2012},
            ],
        value=2004,
        clearable=False), width={'size': 6}),

    dbc.Col(dcc.Dropdown(
        id="dropdown-region",
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
        clearable=False), width={'size': 6})]),
   
    #Row for the density map plot and bar plot   
    dbc.Row([dbc.Col(html.Div(dcc.Graph(id="map-chart")), width={'size': 6}),

           dbc.Col(html.Div(dcc.Graph(id="bar-chart")), width={'size': 6})]),
           
    #Row for the about part and the line plot       
    dbc.Row([dbc.Col(html.Div([
        html.H1(''),
        html.H1('About Zoom'),
        html.Div([
            html.P(''),
            html.P("    Our tool, Zoom, is created for the Road and Safety Authority of the United Kingdom (R&S) with the purpose of understand how the UK’s GDP and economic status, throughout the 2008 recession, effected driving quality in the UK. We would like to help R&S explore how unemployment and economical depressions effect the driving quality of the general public. We believe understanding such a topic would allow R&S to regulate the driving course and syllabus that is taught while getting a license, as it would allow the general public to drive under worse psychological conditions."),
            html.P(''),
            html.P('    We have chosen to driving quality based on casualty severity, the number of casualties, the age groups that are involved in these causalities, and other aspects. We also believe it would be essential to analyze these casualties over different age groups, day of the weeks, and through a multitude of years as well.')
    ])
]), width={'size': 6}),

           dbc.Col(html.Div(dcc.Graph(id="line-chart")), width={'size': 6})]),
           
    #Row for the student information and pie chart
    dbc.Row([dbc.Col(html.Div([html.H1('Imran Makan 1577735', style={'fontSize': 26} ), html.H1('Adam Ibrahim 1542613', style={'fontSize': 26}), html.H1('Bora Ozen 1555685', style={'fontSize': 26}), html.H1('Deniz Erim 1533223', style={'fontSize': 26})]), width={'size': 6}),
           dbc.Col(html.Div(dcc.Graph(id="pie-chart")), width={'size': 6})]),
           ])




#Update function for the bar plot
@app.callback(
    Output("bar-chart", "figure"), 
    [Input("dropdown-region", "value")])
def update_bar(value):
    index = value
    df_bar = Accidents.outFrameBar(index)
     
    #Plotting the bar plot
    fig = fig = px.bar(df_bar, y=df_bar.index.get_level_values(0), 
                       x="count",
                       color= df_bar.index.get_level_values(1),
                       barmode = 'stack',
                       orientation = "h",
                       color_discrete_map={'25 - 34': 'yellow'},
                       range_x = [0, 800000]
                       )
    
    fig.update_layout(
        yaxis={'categoryorder':'array', 'categoryarray':['post-EC','EC','pre-EC']},
        xaxis_title = "Number of Fatal Casualties",
        yaxis_title = "Time Era",
        title = "Fatal Casualties Before, During and After the Economic Crisis"
        )
    
    fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)',paper_bgcolor='rgba(0, 0, 0, 0)',font=dict(
                color="white",
                size=12
            ))
    
    return fig

#Update function for the sunburst plot
@app.callback(
    Output("pie-chart", "figure"), 
    [Input("dropdown-region", "value")])
def update_pie(value):
    index = value
    df_pie = Accidents.outPie(index)
    
    #Plotting the sunburst plot
    fig = px.sunburst(df_pie, path=['Accident year', 'Injury'], 
                  values='Count', color="Accident year",
                  hover_name = 'Accident year',
                  title = 'Sum of Casualties by Age Range',
                  color_discrete_map ={'Fatal Injury': 'red', 'Serious Injury': 'yellow', 'Slight Injury': 'purple'}
                  )

    fig.update_traces(
        go.Sunburst(hovertemplate='%{customdata[0]}<br> Sum:%{value:,.0f} "%{label}<br>%{percentEntry:.2%}"'),
        insidetextorientation='radial')

    fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)',paper_bgcolor='rgba(0, 0, 0, 0)',font=dict(
                color="white",
                size=12
            ))

    fig.update_traces(texttemplate="%{label}<br>%{percentEntry:.2%}")
     
    return fig

#Update function for the line plot
@app.callback(
    Output("line-chart", "figure"), 
    [Input("dropdown-region", "value")])
def update_line_chart(value):
    index = value
    df_line = Accidents.outLine(index)
    
    #Plotting the line plot
    fig = px.line(df_line, x='year', y='total_accident', title="Total Number of Accidents Throughout The Years",
                  labels=dict(total_accident="Total Number of Accidents", year="Year"), markers=True)
    fig.update(layout_yaxis_range = [0,300000])    
    fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)',paper_bgcolor='rgba(0, 0, 0, 0)',font=dict(
                color="white",
                size=12
            ))
    
    return fig

#Update function for the density map plot
@app.callback(
    Output("map-chart", "figure"), 
    [Input("dropdown-year", "value")])
def update_map_chart(value):
    index = value
    df_map = Accidents.outMap(index)
    
    #Plotting the density map plot
    fig = px.density_mapbox(df_map, lat='Latitude', lon='Longitude', z='number_of_casualties', radius=3,
                    center=dict(lat=54.5, lon=-3.943646), zoom=4, range_color=(0, 20),
                    mapbox_style="stamen-terrain", labels=dict(number_of_casualties="Total Number of Casualties"))

    fig.update_layout(
                title = 'Density Map of The Number of Casualties in the UK',
                geo_scope='europe', 
                )

    fig.update_layout(width=750, height=400, margin={"r":0,"t":50,"l":50,"b":0},
            font=dict(
                color="white",
                size=12
            ))

    fig.update_layout(
        geo = dict(
        projection_scale=8, 
        center=dict(lat=54.5, lon=-3.943646),
                ))

    fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)',paper_bgcolor='rgba(0, 0, 0, 0)')
    
    return fig


app.run_server(debug=False, dev_tools_ui=False)