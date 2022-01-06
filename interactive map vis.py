import plotly.graph_objects as go


import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

df = pd.read_csv(r"C:\Users\20203572\Downloads\\Accidents-2009.csv")

df = df[df.latitude != '?']
df = df[df.longitude != '?']
df['Latitude'] = pd.to_numeric(df['latitude'])
df['Longitude'] = pd.to_numeric(df['longitude'])




import plotly.graph_objects as go


dfs = df
import plotly.express as px
fig = px.density_mapbox(df, lat='Latitude', lon='Longitude', z='number_of_casualties', radius=3,
                        center=dict(lat=54.5, lon=-3.943646), zoom=4.2, range_color=(0, 20),
                        mapbox_style="stamen-terrain")

fig.update_layout(
        title = 'Accidents in 2009',
        geo_scope='europe', 
    )



fig.update_layout(width=600, height=400, margin={"r":0,"t":0,"l":0,"b":0})

fig.update_layout(
        geo = dict(
            projection_scale=8, 
            center=dict(lat=54.5, lon=-3.943646),
        ))




app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True, use_reloader=False) 