import pandas as pd
import  plotly.express as px
import  plotly.graph_objects as go
import  numpy as np


def tables():
    df1 = pd.read_excel('Datasets/yearevent.xlsx')
    df2 = pd.read_excel('Datasets/causes.xlsx')
    dfpre = df2.iloc[:4]
    dfpre = dfpre.rename(columns={'Reason': 'Reason No.'})
    dfpost = df2.iloc[4:, :2].reset_index(drop=True)
    dfpost = dfpost.rename(columns={'Reason': 'Reason No.', 'Boy': 'Reasons'})
    dfpost['Reason No.'] = dfpost['Reason No.'] - 3
    return df1 , dfpre , dfpost;



if __name__ == '__main__':
    df = pd.read_excel('Datasets/causes.xlsx');

