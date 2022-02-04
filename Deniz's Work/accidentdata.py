import pandas as pd


class Accidents():
    
    #Reading the final csv file
    df_final = pd.read_csv('FinalDatasetV2.csv', low_memory = False)
    
    #Function which outputs the desired dataset for the bar plot
    def outFrameBar(index):
        df_final = Accidents.df_final.copy()
        
        #Dataset when a specific region is selected from the dropdown menu
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
        
        #Dataset for the entire UK
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
        
    #Function which outputs the desired dataset for the pie chart    
    def outPie(index):
        df_final = Accidents.df_final.copy()
        
        #Dataset when a specific region is selected from the dropdown menu
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
        
        #Dataset for the entire UK
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
    
    #Function which outputs the desired dataset for the density map plot plot        
    def outMap(index):
        
        df_map = Accidents.df_final.copy()
        df_map = df_map[df_map['accident_year'] == index]
        df_map = df_map[df_map.latitude != '?']
        df_map = df_map[df_map.longitude != '?']
        df_map['Latitude'] = pd.to_numeric(df_map['latitude'])
        df_map['Longitude'] = pd.to_numeric(df_map['longitude'])
            
        return df_map
    
    #Function which outputs the desired dataset for the line plot
    def outLine(index):
        df_final = Accidents.df_final.copy()
        
        #Dataset when a specific region is selected from the dropdown menu
        if (index != 0): 
      
            df_1 = df_final
            df_1 = df_1[df_1['police_force'] == index]
            uninc_1 = pd.DataFrame(columns = ['year', 'total_accident'])
            uninc_1['year'] = df_1['accident_year'].unique()
            uninc_1['total_accident'] = df_1.groupby('accident_year').size().tolist()
            
            return uninc_1
        
        #Dataset for the entire UK
        else:
            df_2 = df_final
            uninc_2 = pd.DataFrame(columns = ['year', 'total_accident'])
            uninc_2['year'] = df_2['accident_year'].unique()
            uninc_2['total_accident'] = df_2.groupby('accident_year').size().tolist()
       
        return uninc_2


            
            
            