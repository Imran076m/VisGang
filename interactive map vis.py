import plotly.graph_objects as go


import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

df = pd.read_csv(r"C:\Users\20203572\Downloads\\Accidents-2007-2008.csv")

df = df[df.latitude != '?']
df = df[df.longitude != '?']
df['Latitude'] = pd.to_numeric(df['latitude'])
df['Longitude'] = pd.to_numeric(df['longitude'])
df8 = df[df['accident_year'] == 2008] 
df7 = df[df['accident_year'] == 2007] 
df10 = df[df['accident_year'] == 2010] 
df11 = df[df['accident_year'] == 2011] 




import plotly.graph_objects as go


dfs = df
import plotly.express as px
fig = px.density_mapbox(df7, lat='Latitude', lon='Longitude', z='number_of_casualties', radius=2,
                        center=dict(lat=54.5, lon=-3.943646), zoom=4, range_color=(0, 60),
                        mapbox_style="stamen-terrain")

fig.update_traces(legendgrouptitle_text='Number of Casualties')

fig.update_layout(title = 'Number of Casualties',  geo_scope='europe', width=600, height=400, margin={"r":10,"t":50,"l":10,"b":0}, 
        geo = dict(
            projection_scale=5, 
            center=dict(lat=54.5, lon=-3.943646),
        ))




app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])


app.run_server(debug=True, use_reloader=False) 