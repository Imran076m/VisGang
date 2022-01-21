# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 11:15:58 2022

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
  


    df_1 = pd.read_csv('FinalDataset.csv')
    df_1 = df_1[df_1['police_force'] == index]
    uninc_1 = pd.DataFrame(columns = ['year', 'total_accident','mean_casualty'])
    uninc_1['year'] = df_1['accident_year'].unique()
    uninc_1['total_accident'] = df_1.groupby('accident_year').size().tolist()
    uninc_1['mean_casualty'] = df_1.groupby('accident_year')['casualty_severity'].mean().tolist()

   
    return uninc_1
    
   else:
    df = pd.read_csv('FinalDataset.csv')
    uninc_2 = pd.DataFrame(columns = ['year', 'total_accident','mean_casualty'])
    uninc_2['year'] = df['accident_year'].unique()
    uninc_2['total_accident'] = df.groupby('accident_year').size().tolist()
    uninc_2['mean_casualty'] = df.groupby('accident_year')['casualty_severity'].mean().tolist()
   
    return uninc_2

print(createDFrame(0))