import pandas as pd
import  plotly.express as px
import  plotly.graph_objects as go
import  numpy as np


def preProcessing(df_check):
    df_check = df_check.drop('Unnamed: 0', axis=1)
    return  df_check;

def disList(df):
    lis = df['District Name'].unique().tolist()
    return lis;
def distvals(df , dist):
    dfdist = df[df['District Name'] == dist].reset_index(drop=True)
    avg = dfdist['Total Student Population'].mean()
    avgt = dfdist['Total Teachers Number'].mean();
    stra = dfdist['Total Student Population'] / dfdist['Total Teachers Number']
    stravg = stra.mean()
    return avg,stravg , avgt;



def distGraph(df , dist):
    df_purbam = df[df['District Name'] == dist].reset_index()
    dist = df_purbam['District Name'].iloc[0]
    fig = go.Figure([
        go.Line(name=dist, x=df_purbam.index, y=df_purbam['Dropout rate(%)'])
    ])
    fig.update_xaxes(tickvals=df_purbam.index, ticktext=df_purbam['Year'])
    fig.update_layout(title=f'Dropout rates of {dist}', xaxis_title='Year', yaxis_title='Dropout Rate')
    fig2 = go.Figure([
        go.Line(name=dist, x=df_purbam.index, y=df_purbam['Total Student Population'])
    ]);
    fig2.update_xaxes(tickvals=df_purbam.index, ticktext=df_purbam['Year'])
    fig2.update_layout(title=f'Student Count analysis on {dist}', xaxis_title='Year', yaxis_title='Total Student Count')
    return fig , fig2;
def overallGraph(df):
    lis = [];
    df_purbam = df[df['District Name'] == 'Howrah'].reset_index()
    for i in df['District Name'].unique():
        temp = df[df['District Name'] == i].reset_index();
        fig = go.Line(name=i, x=temp.index, y=temp['Dropout rate(%)'])
        lis.append(fig)

    fig1 = go.Figure(lis);
    fig1.update_xaxes(tickvals=df_purbam.index, ticktext=df_purbam['Year'])
    fig1.update_layout(title=f'Dropout Analysis on All Districts', xaxis_title='Year', yaxis_title='Dropout Rate')
    lis = [];
    for i in df['District Name'].unique():
        temp = df[df['District Name'] == i].reset_index();
        fig = go.Line(name=i, x=temp.index, y=temp['Total Student Population'])
        lis.append(fig)

    fig2= go.Figure(lis);
    fig2.update_xaxes(tickvals=df_purbam.index, ticktext=df_purbam['Year'])
    fig2.update_layout(title='Student Count', xaxis_title='Year', yaxis_title='Total Student Count')
    return fig1 , fig2;


def compDist(df , dist1, dist2):
    temp1 = df[df['District Name'] == dist1].reset_index();
    temp2 = df[df['District Name'] == dist2].reset_index();
    fig1 = go.Line(name=dist1, x=temp1.index, y=temp1['Dropout rate(%)'])
    fig2 = go.Line(name=dist2, x=temp2.index, y=temp2['Dropout rate(%)'])
    fig = go.Figure([fig1, fig2]);
    fig.update_xaxes(tickvals=temp1.index, ticktext=temp1['Year'])
    fig.update_layout(title=f'Dropout Analysis {dist1} vs {dist2}', xaxis_title='Year', yaxis_title='Dropout Rate')
    fig.update_layout(hovermode="x unified")
    return fig







