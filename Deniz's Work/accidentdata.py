import pandas as pd

class Accidents():
    
    df_acc_pre = pd.read_csv("C:/Users/deniz/Desktop/TUe/Year 2/Q2/JBI100 - Visualisations/Databases/Casualty-2004-2006.csv", low_memory = False)
    df_acc_on = pd.read_csv("C:/Users/deniz/Desktop/TUe/Year 2/Q2/JBI100 - Visualisations/Databases/Casualty-2007-2009.csv", low_memory = False)
    df_acc_post = pd.read_csv("C:/Users/deniz/Desktop/TUe/Year 2/Q2/JBI100 - Visualisations/Databases/Casualty-2010-2012.csv", low_memory = False)
    df_po_pre = pd.read_csv("C:/Users/deniz/Desktop/TUe/Year 2/Q2/JBI100 - Visualisations/Databases/Accidents-2004-2006.csv", low_memory = False)
    df_po_on = pd.read_csv("C:/Users/deniz/Desktop/TUe/Year 2/Q2/JBI100 - Visualisations/Databases/Accidents-2007-2009.csv", low_memory = False)
    df_po_post = pd.read_csv("C:/Users/deniz/Desktop/TUe/Year 2/Q2/JBI100 - Visualisations/Databases/Accidents-2010-2012.csv", low_memory = False)
    def outFrameBar(index):
        df_acc_pre = Accidents.df_acc_pre
        df_acc_on = Accidents.df_acc_on
        df_acc_post = Accidents.df_acc_post
        df_po_pre = Accidents.df_po_pre
        df_po_on = Accidents.df_po_on
        df_po_post = Accidents.df_po_post
        if index != 0:
            
            df_force_on = df_po_on[['police_force', 'accident_index']].set_index('accident_index')
            df_acc_local_on = df_acc_on[df_acc_on['casualty_severity'] == 1].set_index('accident_index')
            df_acc_local_on = df_acc_local_on.join(df_force_on)
            df_acc_fatal_on = df_acc_local_on[df_acc_local_on['police_force'] == index]
            df_age_on = df_acc_fatal_on.pivot_table(columns=['age_band_of_casualty'], aggfunc='size')
            df_age_on = df_age_on.to_frame()
            df_age_on['time'] = "EC"
            df_age_on = df_age_on.rename(index={-1: "Missing data or out of range", 1: "0-5", 2: "6-10", 3: "11-15", 4: "15-20", 5: "21-25",
                                                6: "26-35", 7: "36-45", 8: "46-55", 9: "56-65", 10: "66-75", 11: "75+"})
            df_age_on = df_age_on.rename(columns={0: "count"})
            df_age_on = df_age_on.reset_index()
            df_age_on = df_age_on.set_index(['time', 'age_band_of_casualty']) 
            
            
            df_force_pre = df_po_pre[['police_force', 'accident_index']].set_index('accident_index')
            df_acc_local_pre = df_acc_pre[df_acc_pre['casualty_severity'] == 1].set_index('accident_index')
            df_acc_local_pre = df_acc_local_pre.join(df_force_pre)
            df_acc_fatal_pre = df_acc_local_pre[df_acc_local_pre['police_force'] == index]
            df_age_pre = df_acc_fatal_pre.pivot_table(columns=['age_band_of_casualty'], aggfunc='size')
            df_age_pre = df_age_pre.to_frame()
            df_age_pre['time'] = "pre-EC"
            df_age_pre = df_age_pre.rename(index={-1: "Missing data or out of range", 1: "0-5", 2: "6-10", 3: "11-15", 4: "15-20", 5: "21-25",
                                                6: "26-35", 7: "36-45", 8: "46-55", 9: "56-65", 10: "66-75", 11: "75+"})
            df_age_pre = df_age_pre.rename(columns={0: "count"})
            df_age_pre = df_age_pre.reset_index()
            df_age_pre = df_age_pre.set_index(['time', 'age_band_of_casualty'])
            
            
            df_force_post = df_po_post[['police_force', 'accident_index']].set_index('accident_index')
            df_acc_local_post = df_acc_post[df_acc_post['casualty_severity'] == 1].set_index('accident_index')
            df_acc_local_post = df_acc_local_post.join(df_force_post)
            df_acc_fatal_post = df_acc_local_post[df_acc_local_post['police_force'] == index]
            df_age_post = df_acc_fatal_post.pivot_table(columns=['age_band_of_casualty'], aggfunc='size')
            df_age_post = df_age_post.to_frame()
            df_age_post['time'] = "post-EC"
            df_age_post = df_age_post.rename(index={-1: "Missing data or out of range", 1: "0-5", 2: "6-10", 3: "11-15", 4: "15-20", 5: "21-25",
                                                6: "26-35", 7: "36-45", 8: "46-55", 9: "56-65", 10: "66-75", 11: "75+"})
            df_age_post = df_age_post.rename(columns={0: "count"})
            df_age_post = df_age_post.reset_index()
            df_age_post = df_age_post.set_index(['time', 'age_band_of_casualty']) 
            
            
            frames = [df_age_post, df_age_on, df_age_pre]
            df_bar = pd.concat(frames)
            return df_bar
        
        else:
            df_acc_fatal_on = df_acc_on[df_acc_on['casualty_severity'] == 1]
            df_age_on = df_acc_fatal_on.pivot_table(columns=['age_band_of_casualty'], aggfunc='size')
            df_age_on = df_age_on.to_frame()
            df_age_on['time'] = ['EC', 'EC','EC','EC','EC','EC','EC','EC','EC','EC','EC','EC',]
            df_age_on = df_age_on.rename(index={-1: "Missing data or out of range", 1: "0-5", 2: "6-10", 3: "11-15", 4: "15-20", 5: "21-25",
                                                6: "26-35", 7: "36-45", 8: "46-55", 9: "56-65", 10: "66-75", 11: "75+"})
            df_age_on = df_age_on.rename(columns={0: "count"})
            df_age_on = df_age_on.reset_index()
            df_age_on = df_age_on.set_index(['time', 'age_band_of_casualty'])
            
            
            df_acc_fatal_pre = df_acc_pre[df_acc_pre['casualty_severity'] == 1]
            df_age_pre = df_acc_fatal_pre.pivot_table(columns=['age_band_of_casualty'], aggfunc='size')
            df_age_pre = df_age_pre.to_frame()
            df_age_pre['time'] = ['pre-EC', 'pre-EC','pre-EC','pre-EC','pre-EC','pre-EC','pre-EC','pre-EC','pre-EC','pre-EC','pre-EC','pre-EC',]
            df_age_pre = df_age_pre.rename(index={-1: "Missing data or out of range", 1: "0-5", 2: "6-10", 3: "11-15", 4: "15-20", 5: "21-25",
                                              6: "26-35", 7: "36-45", 8: "46-55", 9: "56-65", 10: "66-75", 11: "75+"})
            df_age_pre = df_age_pre.rename(columns={0 : "count"})
            df_age_pre = df_age_pre.reset_index()
            df_age_pre = df_age_pre.set_index(['time', 'age_band_of_casualty']) 
            
            df_acc_fatal_post = df_acc_post[df_acc_post['casualty_severity'] == 1]
            df_age_post = df_acc_fatal_post.pivot_table(columns=['age_band_of_casualty'], aggfunc='size')
            df_age_post = df_age_post.to_frame()
            df_age_post['time'] = [ 'post-EC','post-EC','post-EC','post-EC','post-EC','post-EC','post-EC','post-EC','post-EC','post-EC','post-EC',]
            df_age_post = df_age_post.rename(index={-1: "Missing data or out of range", 1: "0-5", 2: "6-10", 3: "11-15", 4: "15-20", 5: "21-25",
                                              6: "26-35", 7: "36-45", 8: "46-55", 9: "56-65", 10: "66-75", 11: "75+"})
            df_age_post = df_age_post.rename(columns={0 : "count"})
            df_age_post = df_age_post.reset_index()
            df_age_post = df_age_post.set_index(['time', 'age_band_of_casualty'])            
            
            frames = [df_age_post, df_age_on, df_age_pre]
            df_bar = pd.concat(frames)
            return df_bar
        

            
            
            