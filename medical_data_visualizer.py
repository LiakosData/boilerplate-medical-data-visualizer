import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline

# 1
df = pd.read_csv(r'C:\Users\ilias\Documents\PythonProjects\medical_examination.csv')

# 2
BMI = df['weight'] / (df['height'] /100) **2
df['BMI'] =BMI
df['overweight'] = np.where(df['BMI']>25, 1, 0)

#3
df['cholesterol'] = np.where(df['cholesterol'] > 1, 1, 0)
df['gluc'] = np.where(df['gluc'] >1, 1, 0,)
df.rename(columns={'gluc' : 'glucose', 'alco': 'alcohol'}, inplace=True)

#4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(
    df,
    id_vars = ['cardio'],
    value_vars = ['cholesterol', 'glucose', 'smoke', 'alcohol', 'active', 'overweight'])
   
    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'])['value'].count().reset_index(name='total')


    # 8
    fig =  sns.catplot(
        x="variable",
        y="total",
        hue="value",
        col="cardio",
        data=df_cat,
        kind="bar",
        height=5,
        aspect=1.2)
   

    plt.show()
    # 9
    fig.savefig('catplot.png')
    return fig
fig = draw_cat_plot() 

# 10
def draw_heat_map():
    # 11
    df_heat = df[
    (df['ap_lo'] <= df['ap_hi']) &
    (df['height'] >= df['height'].quantile(0.025)) &
    (df['height']<= df['height'].quantile(0.975)) &
    (df['weight']>= df['weight'].quantile(0.025)) &
    (df['weight']<= df['weight'].quantile(0.975))
    ]
#12
    corr = df_heat.corr()

 # 13
    mask =np.triu(np.ones_like(corr, dtype=bool))
    

 # 14
    fig, ax = plt.subplots(figsize=(10, 8))


    #15 plot corr using heatmap
        sns.heatmap(
        corr,
        mask=mask,
        ax = ax,
        cmap='coolwarm',
        annot=True,
        fmt = ".1f")
        
        

     # 16
    fig.savefig('heatmap.png')
    return fig
draw_heat_map()
