# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 19:01:29 2021

@author: 20201349
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
#df_acc_local_on = df_acc_on[df_acc_on['police_force'] == index]

def createDFrame(index):
   if (index != 0): 
    df = pd.read_csv('Accidents-2007-2008.csv')
    df = df[df['police_force'] == index]
    uninc = pd.DataFrame(columns = ['year', 'total_accident','mean_severity','mean_casualty'])
    uninc['year'] = df['accident_year'].unique()
    uninc['total_accident'] = df.groupby('accident_year').size().tolist()
    uninc['mean_severity'] = df.groupby('accident_year')['accident_severity'].mean().tolist()
    uninc['mean_casualty'] = df.groupby('accident_year')['number_of_casualties'].mean().tolist()


    df_1 = pd.read_csv('Accidents-2005-2006.csv')
    df_1 = df_1[df_1['police_force'] == index]
    uninc_1 = pd.DataFrame(columns = ['year', 'total_accident','mean_severity','mean_casualty'])
    uninc_1['year'] = df_1['accident_year'].unique()
    uninc_1['total_accident'] = df_1.groupby('accident_year').size().tolist()
    uninc_1['mean_severity'] = df_1.groupby('accident_year')['accident_severity'].mean().tolist()
    uninc_1['mean_casualty'] = df_1.groupby('accident_year')['number_of_casualties'].mean().tolist()

    df_3 = pd.read_csv('Accidents-2009.csv')
    df_3 = df_3[df_3['police_force'] == index]
    uninc_3 = pd.DataFrame(columns = ['year', 'total_accident','mean_severity','mean_casualty'])
    uninc_3['year'] = df_3['accident_year'].unique()
    uninc_3['total_accident'] = df_3.groupby('accident_year').size().tolist()
    uninc_3['mean_severity'] = df_3.groupby('accident_year')['accident_severity'].mean().tolist()
    uninc_3['mean_casualty'] = df_3.groupby('accident_year')['number_of_casualties'].mean().tolist()

    df_2 = pd.read_csv('Accidents-2010-2011.csv')
    df_2 = df_2[df_2['police_force'] == index]
    uninc_2 = pd.DataFrame(columns = ['year', 'total_accident','mean_severity','mean_casualty'])
    uninc_2['year'] = df_2['accident_year'].unique()
    uninc_2['total_accident'] = df_2.groupby('accident_year').size().tolist()
    uninc_2['mean_severity'] = df_2.groupby('accident_year')['accident_severity'].mean().tolist()
    uninc_2['mean_casualty'] = df_2.groupby('accident_year')['number_of_casualties'].mean().tolist()

    df_all_rows = pd.concat([uninc_1, uninc, uninc_2],ignore_index=True)
    return df_all_rows
    
   else:
    df = pd.read_csv('Accidents-2007-2008.csv')
    uninc = pd.DataFrame(columns = ['year', 'total_accident','mean_severity','mean_casualty'])
    uninc['year'] = df['accident_year'].unique()
    uninc['total_accident'] = df.groupby('accident_year').size().tolist()
    uninc['mean_severity'] = df.groupby('accident_year')['accident_severity'].mean().tolist()
    uninc['mean_casualty'] = df.groupby('accident_year')['number_of_casualties'].mean().tolist()

    df_1 = pd.read_csv('Accidents-2005-2006.csv')
    uninc_1 = pd.DataFrame(columns = ['year', 'total_accident','mean_severity','mean_casualty'])
    uninc_1['year'] = df_1['accident_year'].unique()
    uninc_1['total_accident'] = df_1.groupby('accident_year').size().tolist()
    uninc_1['mean_severity'] = df_1.groupby('accident_year')['accident_severity'].mean().tolist()
    uninc_1['mean_casualty'] = df_1.groupby('accident_year')['number_of_casualties'].mean().tolist()

    df_3 = pd.read_csv('Accidents-2009.csv')
    uninc_3 = pd.DataFrame(columns = ['year', 'total_accident','mean_severity','mean_casualty'])
    uninc_3['year'] = df_3['accident_year'].unique()
    uninc_3['total_accident'] = df_3.groupby('accident_year').size().tolist()
    uninc_3['mean_severity'] = df_3.groupby('accident_year')['accident_severity'].mean().tolist()
    uninc_3['mean_casualty'] = df_3.groupby('accident_year')['number_of_casualties'].mean().tolist()

    df_2 = pd.read_csv('Accidents-2010-2011.csv')
    uninc_2 = pd.DataFrame(columns = ['year', 'total_accident','mean_severity','mean_casualty'])
    uninc_2['year'] = df_2['accident_year'].unique()
    uninc_2['total_accident'] = df_2.groupby('accident_year').size().tolist()
    uninc_2['mean_severity'] = df_2.groupby('accident_year')['accident_severity'].mean().tolist()
    uninc_2['mean_casualty'] = df_2.groupby('accident_year')['number_of_casualties'].mean().tolist()

    df_all_rows = pd.concat([uninc_1, uninc, uninc_2],ignore_index=True)
    return df_all_rows
        
    
print(createDFrame(3))


