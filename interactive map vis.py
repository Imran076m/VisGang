import geopandas as gpd

dataset = "C:\\Users\\20203572\\Desktop\\Vis\\Accidents-2007-2008.csv"
df = gpd.read_file(dataset)

#df.head()



import pandas as pd

df = df[df.latitude != '?']
df = df[df.longitude != '?']
#df['Latitude'] = pd.to_numeric(df['Latitude'])

#df['Longitude'] = pd.to_numeric(df['Longitude'])
#df


df['Latitude'] = pd.to_numeric(df['latitude'])

df['Longitude'] = pd.to_numeric(df['longitude'])
#df


import folium
map = folium.Map(location=[-0.209082	,51.506187], zoom_start=3)
#loca = df.head()
df = df.dropna(subset=['Latitude'])
for _, i in df.loc[0:100].iterrows():
    print(1)
    folium.Marker(location=[i['Latitude'], i['Longitude']]).add_to(map)
map
 




#gdf = gpd.GeoDataFrame(
#    df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude))






#world = gpd.read_file(
#    gpd.datasets.get_path('naturalearth_lowres')
#)
#uk = world.query('country == "United Kingdom"')
#import folium
#import matplotlib
#import mapclassify
#world.columns=['pop_est', 'continent', 'name', 'CODE', 'gdp_md_est', 'geometry']

#uk = world[world['name'] == 'United Kingdom']
#gdf.explore()
#ax = uk.plot()
#gdf.head().plot(ax = ax)
#uk.explore()