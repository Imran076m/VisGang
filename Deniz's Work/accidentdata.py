import pandas as pd
import plotly.express as px

class Accidents():
    
    #df_acc_pre = pd.read_csv("C:/Users/deniz/Desktop/TUe/Year 2/Q2/JBI100 - Visualisations/Databases/Casualty-2004-2006.csv", low_memory = False)
    #df_acc_on = pd.read_csv("C:/Users/deniz/Desktop/TUe/Year 2/Q2/JBI100 - Visualisations/Databases/Casualty-2007-2009.csv", low_memory = False)
    #df_acc_post = pd.read_csv("C:/Users/deniz/Desktop/TUe/Year 2/Q2/JBI100 - Visualisations/Databases/Casualty-2010-2012.csv", low_memory = False)
    #df_po_pre = pd.read_csv("C:/Users/deniz/Desktop/TUe/Year 2/Q2/JBI100 - Visualisations/Databases/Accidents-2004-2006.csv", low_memory = False)
    #df_po_on = pd.read_csv("C:/Users/deniz/Desktop/TUe/Year 2/Q2/JBI100 - Visualisations/Databases/Accidents-2007-2009.csv", low_memory = False)
    #df_po_post = pd.read_csv("C:/Users/deniz/Desktop/TUe/Year 2/Q2/JBI100 - Visualisations/Databases/Accidents-2010-2012.csv", low_memory = False)
    df_final = pd.read_csv('Dataset\FinalDatasetV2.csv', low_memory = False)
    def outFrameBar(index):
        df_final = Accidents.df_final.copy()
        if index != 0:
            
            df_acc_on = df_final[(df_final["accident_year"] >= 2007) & (df_final["accident_year"] <= 2009)] 
            df_acc_fatal_on = df_acc_on[df_acc_on['police_force'] == index]
            df_acc_fatal_on["time"] = "EC"
            df_acc_fatal_on = df_acc_fatal_on.set_index("time")
            df_age_on = df_acc_fatal_on.groupby(["time", (pd.cut(df_acc_fatal_on["age_of_casualty"], [0, 16, 24, 34, 50, 64, 100]))]).count()
            df_age_on = df_age_on[["police_force"]]
            df_age_on = df_age_on.rename(columns={"police_force": "count"})
            df_age_on.index = df_age_on.index.set_levels(df_age_on.index.levels[-1].astype(str), level=-1)
            df_age_on = df_age_on.rename(index={"(0, 16]" :"0 - 16",
                                                "(16, 24]":"17 - 24",
                                                "(24, 34]":"25 - 34",
                                                "(34, 50]":"35 - 50",
                                                "(50, 64]":"51 - 64",
                                                "(64, 100]": "64+"})
            
            df_acc_pre = df_final[(df_final["accident_year"] >= 2004) & (df_final["accident_year"] <= 2006)] 
            df_acc_fatal_pre = df_acc_pre[df_acc_pre['police_force'] == index]
            df_acc_fatal_pre["time"] = "pre-EC"
            df_acc_fatal_pre = df_acc_fatal_pre.set_index("time")
            df_age_pre = df_acc_fatal_pre.groupby(["time", (pd.cut(df_acc_fatal_pre["age_of_casualty"], [0, 16, 24, 34, 50, 64, 100]))]).count()
            df_age_pre = df_age_pre[["police_force"]]
            df_age_pre = df_age_pre.rename(columns={"police_force": "count"})
            df_age_pre.index = df_age_pre.index.set_levels(df_age_pre.index.levels[-1].astype(str), level=-1)
            df_age_pre = df_age_pre.rename(index={"(0, 16]" :"0 - 16",
                                                "(16, 24]":"17 - 24",
                                                "(24, 34]":"25 - 34",
                                                "(34, 50]":"35 - 50",
                                                "(50, 64]":"51 - 64",
                                                "(64, 100]": "64+"})
            
            df_acc_post = df_final[(df_final["accident_year"] >= 2010) & (df_final["accident_year"] <= 2012)] 
            df_acc_fatal_post = df_acc_post[df_acc_post['police_force'] == index]
            df_acc_fatal_post["time"] = "post-EC"
            df_acc_fatal_post = df_acc_fatal_post.set_index("time")
            df_age_post = df_acc_fatal_post.groupby(["time", (pd.cut(df_acc_fatal_post["age_of_casualty"], [0, 16, 24, 34, 50, 64, 100]))]).count()
            df_age_post = df_age_post[["police_force"]]
            df_age_post = df_age_post.rename(columns={"police_force": "count"})
            df_age_post.index = df_age_post.index.set_levels(df_age_post.index.levels[-1].astype(str), level=-1)
            df_age_post = df_age_post.rename(index={"(0, 16]" :"0 - 16",
                                                "(16, 24]":"17 - 24",
                                                "(24, 34]":"25 - 34",
                                                "(34, 50]":"35 - 50",
                                                "(50, 64]":"51 - 64",
                                                "(64, 100]": "64+"})
            
            frames = [df_age_post, df_age_on, df_age_pre]
            df_bar = pd.concat(frames)
            return df_bar
            
        else:
            
            
            df_acc_on = df_final[(df_final["accident_year"] >= 2007) & (df_final["accident_year"] <= 2009)] 
            df_acc_on["time"] = "EC"
            df_acc_fatal_on = df_acc_on.set_index("time")
            df_age_on = df_acc_fatal_on.groupby(["time", (pd.cut(df_acc_fatal_on["age_of_casualty"], [0, 16, 24, 34, 50, 64, 100]))]).count()
            df_age_on = df_age_on[["police_force"]]
            df_age_on = df_age_on.rename(columns={"police_force": "count"})
            df_age_on.index = df_age_on.index.set_levels(df_age_on.index.levels[-1].astype(str), level=-1)
            df_age_on = df_age_on.rename(index={"(0, 16]" :"0 - 16",
                                                "(16, 24]":"17 - 24",
                                                "(24, 34]":"25 - 34",
                                                "(34, 50]":"35 - 50",
                                                "(50, 64]":"51 - 64",
                                                "(64, 100]": "64+"})
            
            df_acc_pre = df_final[(df_final["accident_year"] >= 2004) & (df_final["accident_year"] <= 2006)] 
            df_acc_pre["time"] = "pre-EC"
            df_acc_fatal_pre = df_acc_pre.set_index("time")
            df_age_pre = df_acc_fatal_pre.groupby(["time", (pd.cut(df_acc_fatal_pre["age_of_casualty"], [0, 16, 24, 34, 50, 64, 100]))]).count()
            df_age_pre = df_age_pre[["police_force"]]
            df_age_pre = df_age_pre.rename(columns={"police_force": "count"})
            df_age_pre.index = df_age_pre.index.set_levels(df_age_pre.index.levels[-1].astype(str), level=-1)
            df_age_pre = df_age_pre.rename(index={"(0, 16]" :"0 - 16",
                                                "(16, 24]":"17 - 24",
                                                "(24, 34]":"25 - 34",
                                                "(34, 50]":"35 - 50",
                                                "(50, 64]":"51 - 64",
                                                "(64, 100]": "64+"})
            
            df_acc_post = df_final[(df_final["accident_year"] >= 2010) & (df_final["accident_year"] <= 2012)] 
            df_acc_post["time"] = "post-EC"
            df_acc_fatal_post = df_acc_post.set_index("time")
            df_age_post = df_acc_fatal_post.groupby(["time", (pd.cut(df_acc_fatal_post["age_of_casualty"], [0, 16, 24, 34, 50, 64, 100]))]).count()
            df_age_post = df_age_post[["police_force"]]
            df_age_post = df_age_post.rename(columns={"police_force": "count"})
            df_age_post.index = df_age_post.index.set_levels(df_age_post.index.levels[-1].astype(str), level=-1)
            df_age_post = df_age_post.rename(index={"(0, 16]" :"0 - 16",
                                                "(16, 24]":"17 - 24",
                                                "(24, 34]":"25 - 34",
                                                "(34, 50]":"35 - 50",
                                                "(50, 64]":"51 - 64",
                                                "(64, 100]": "64+"})
            
            
            frames = [df_age_post, df_age_on, df_age_pre]
            df_bar = pd.concat(frames)
            return df_bar
        
        
    def outPie(index):
        df_final = Accidents.df_final.copy()
        
        if index != 0:
            df = df_final[['accident_year', 'casualty_severity', 'age_of_casualty', 'police_force']]
            drop = df[df.age_of_casualty == -1]
            df.drop(drop.index, inplace=True)
            df = df[df['police_force'] == index]

            g1 = df.loc[(df['accident_year'] >= 2004) & (df['accident_year'] <= 2006)]
            g1 = g1.groupby([(pd.cut(g1["casualty_severity"], [0, 1, 2, 3]))]).count()
            g1.drop(['casualty_severity', 'age_of_casualty'], axis=1, inplace=True)
            g1 = g1.reset_index()
            g1['Accident year'] = "2004 - 2006"
        
            g2 = df.loc[(df['accident_year'] >= 2007) & (df['accident_year'] <= 2009)]
            g2 = g2.groupby([(pd.cut(g2["casualty_severity"], [0, 1, 2, 3]))]).count()
            g2.drop(['casualty_severity', 'age_of_casualty'], axis=1, inplace=True)
            g2 = g2.reset_index()
            g2['Accident year'] = "2007 - 2009"
        
            g3 = df.loc[(df['accident_year'] >= 2010) & (df['accident_year'] <= 2012)]
            g3 = g3.groupby([(pd.cut(g3["casualty_severity"], [0, 1, 2, 3]))]).count()
            g3.drop(['casualty_severity', 'age_of_casualty'], axis=1, inplace=True)
            g3 = g3.reset_index()
            g3['Accident year'] = "2010 - 2012"
        
            groups = [g1, g2, g3]
            new_df = pd.concat(groups)
            new_df['casualty_severity'] = new_df['casualty_severity'].astype('str')
            new_df['casualty_severity'] = new_df['casualty_severity'].convert_dtypes()
            new_df['casualty_severity'] = new_df['casualty_severity'].replace(
                            {  "(0, 1]" : "Slight Injury",
                               "(1, 2]" : "Serious Injury",
                               "(2, 3]" : "Fatal Injury"
                             })
            new_df = new_df.rename(columns={'casualty_severity': 'Injury', 'accident_year': 'Count'})
            return new_df
        
        else:
            
            df = df_final[['accident_year', 'casualty_severity', 'age_of_casualty']]
            drop = df[df.age_of_casualty == -1]
            df.drop(drop.index, inplace=True)

            g1 = df.loc[(df['accident_year'] >= 2004) & (df['accident_year'] <= 2006)]
            g1 = g1.groupby([(pd.cut(g1["casualty_severity"], [0, 1, 2, 3]))]).count()
            g1.drop(['casualty_severity', 'age_of_casualty'], axis=1, inplace=True)
            g1 = g1.reset_index()
            g1['Accident year'] = "2004 - 2006"
        
            g2 = df.loc[(df['accident_year'] >= 2007) & (df['accident_year'] <= 2009)]
            g2 = g2.groupby([(pd.cut(g2["casualty_severity"], [0, 1, 2, 3]))]).count()
            g2.drop(['casualty_severity', 'age_of_casualty'], axis=1, inplace=True)
            g2 = g2.reset_index()
            g2['Accident year'] = "2007 - 2009"
        
            g3 = df.loc[(df['accident_year'] >= 2010) & (df['accident_year'] <= 2012)]
            g3 = g3.groupby([(pd.cut(g3["casualty_severity"], [0, 1, 2, 3]))]).count()
            g3.drop(['casualty_severity', 'age_of_casualty'], axis=1, inplace=True)
            g3 = g3.reset_index()
            g3['Accident year'] = "2010 - 2012"
        
            groups = [g1, g2, g3]
            new_df = pd.concat(groups)
            new_df['casualty_severity'] = new_df['casualty_severity'].astype('str')
            new_df['casualty_severity'] = new_df['casualty_severity'].convert_dtypes()
            new_df['casualty_severity'] = new_df['casualty_severity'].replace(
                            {  "(0, 1]" : "Slight Injury",
                               "(1, 2]" : "Serious Injury",
                               "(2, 3]" : "Fatal Injury"
                               })
            new_df = new_df.rename(columns={'casualty_severity': 'Injury', 'accident_year': 'Count'})
            return new_df
            
    def outMap(index):
        
        df_map = Accidents.df_final.copy()
        df_map = df_map[df_map['accident_year'] == index]
        df_map = df_map[df_map.latitude != '?']
        df_map = df_map[df_map.longitude != '?']
        df_map['Latitude'] = pd.to_numeric(df_map['latitude'])
        df_map['Longitude'] = pd.to_numeric(df_map['longitude'])
            
        return df_map
    
    def outLine(index):
        df_final = Accidents.df_final.copy()
        
        if (index != 0): 
      
            df_1 = df_final
            df_1 = df_1[df_1['police_force'] == index]
            uninc_1 = pd.DataFrame(columns = ['year', 'total_accident','mean_casualty'])
            uninc_1['year'] = df_1['accident_year'].unique()
            uninc_1['total_accident'] = df_1.groupby('accident_year').size().tolist()
            uninc_1['mean_casualty'] = df_1.groupby('accident_year')['casualty_severity'].mean().tolist()
    
            return uninc_1
        
        else:
            df_2 = df_final
            uninc_2 = pd.DataFrame(columns = ['year', 'total_accident','mean_casualty'])
            uninc_2['year'] = df_2['accident_year'].unique()
            uninc_2['total_accident'] = df_2.groupby('accident_year').size().tolist()
            uninc_2['mean_casualty'] = df_2.groupby('accident_year')['casualty_severity'].mean().tolist()
       
        return uninc_2


            
            
            