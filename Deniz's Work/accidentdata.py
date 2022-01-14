import dash
from dash import dcc
from dash import html
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np

class Accidents():
    
    df_acc_pre = pd.read_csv("C:/Users/deniz/Desktop/TUe/Year 2/Q2/JBI100 - Visualisations/Databases/Accidents-2005-2006.csv", low_memory = False)
    df_acc_on = pd.read_csv("C:/Users/deniz/Desktop/TUe/Year 2/Q2/JBI100 - Visualisations/Databases/Accidents-2007-2008.csv", low_memory = False)
    df_acc_post = pd.read_csv("C:/Users/deniz/Desktop/TUe/Year 2/Q2/JBI100 - Visualisations/Databases/Accidents-2010-2011.csv", low_memory = False)
    def outFrameBar(index):
        df_acc_pre = Accidents.df_acc_pre
        df_acc_on = Accidents.df_acc_on
        df_acc_post = Accidents.df_acc_post
        if index != 0:
            
            df_acc_local_on = df_acc_on[df_acc_on['police_force'] == index]
            count_acc_local_on = len(df_acc_local_on[df_acc_local_on['accident_severity'] == 1].value_counts())
            df_fatal_acc_on = pd.DataFrame(np.array([count_acc_local_on]), columns = ['Count'])
            df_fatal_acc_on = df_fatal_acc_on.set_axis(['EC'], axis = 0)
            df_fatal_acc_on['Time'] = ['EC'] 
            
            df_acc_local_pre = df_acc_pre[df_acc_pre['police_force'] == index]
            count_acc_local_pre = len(df_acc_local_pre[df_acc_local_pre['accident_severity'] == 1].value_counts())
            df_fatal_acc_pre = pd.DataFrame(np.array([count_acc_local_pre]), columns = ['Count'])
            df_fatal_acc_pre = df_fatal_acc_pre.set_axis(['EC'], axis = 0)
            df_fatal_acc_pre['Time'] = ['Pre-EC'] 
            
            df_acc_local_post = df_acc_post[df_acc_post['police_force'] == index]
            count_acc_local_post = len(df_acc_local_post[df_acc_local_post['accident_severity'] == 1].value_counts())
            df_fatal_acc_post = pd.DataFrame(np.array([count_acc_local_post]), columns = ['Count'])
            df_fatal_acc_post = df_fatal_acc_post.set_axis(['EC'], axis = 0)
            df_fatal_acc_post['Time'] = ['Post-EC'] 
            
            frames = [df_fatal_acc_post, df_fatal_acc_on, df_fatal_acc_pre]
            df_bar = pd.concat(frames)
            return df_bar
        
        else:
            count_acc_local_on = len(df_acc_on[df_acc_on['accident_severity'] == 1].value_counts())
            df_fatal_acc_on = pd.DataFrame(np.array([count_acc_local_on]), columns = ['Count'])
            df_fatal_acc_on = df_fatal_acc_on.set_axis(['EC'], axis = 0)
            df_fatal_acc_on['Time'] = ['EC']
            
            count_acc_local_pre = len(df_acc_pre[df_acc_pre['accident_severity'] == 1].value_counts())
            df_fatal_acc_pre = pd.DataFrame(np.array([count_acc_local_pre]), columns = ['Count'])
            df_fatal_acc_pre = df_fatal_acc_pre.set_axis(['EC'], axis = 0)
            df_fatal_acc_pre['Time'] = ['Pre-EC']
            
            count_acc_local_post = len(df_acc_post[df_acc_post['accident_severity'] == 1].value_counts())
            df_fatal_acc_post = pd.DataFrame(np.array([count_acc_local_post]), columns = ['Count'])
            df_fatal_acc_post = df_fatal_acc_post.set_axis(['EC'], axis = 0)
            df_fatal_acc_post['Time'] = ['Post-EC'] 
            
            frames = [df_fatal_acc_post, df_fatal_acc_on, df_fatal_acc_pre]
            df_bar = pd.concat(frames)
            return df_bar
        

            
            
            