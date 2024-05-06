import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np


def GetGraph(df , dist):
    df_purbam = df[df['Cast'] == dist].reset_index()
    dist = df_purbam['Cast'].iloc[0]
    fig = go.Figure([
        go.Line(name=dist, x=df_purbam.index, y=df_purbam['Dropout rate(%)'])
    ])
    fig.update_xaxes(tickvals=df_purbam.index, ticktext=df_purbam['Year'])
    fig.update_layout(title=f'Dropout rates of {dist}', xaxis_title='Year', yaxis_title='Dropout Rate')
    return fig;


def compCast(df , dist1, dist2):
    temp1 = df[df['Cast'] == dist1].reset_index();
    temp2 = df[df['Cast'] == dist2].reset_index();
    fig1 = go.Line(name=dist1, x=temp1.index, y=temp1['Dropout rate(%)'])
    fig2 = go.Line(name=dist2, x=temp2.index, y=temp2['Dropout rate(%)'])
    fig = go.Figure([fig1, fig2]);
    fig.update_xaxes(tickvals=temp1.index, ticktext=temp1['Year'])
    fig.update_layout(title=f'Dropout Analysis {dist1} vs {dist2}', xaxis_title='Year', yaxis_title='Dropout Rate')
    fig.update_layout(hovermode="x unified")
    return fig


def overallGraph(df):
    lis = [];
    df_purbam = df[df['Cast'] == 'SC'].reset_index()
    for i in df['Cast'].unique():
        temp = df[df['Cast'] == i].reset_index();
        fig = go.Line(name=i, x=temp.index, y=temp['Dropout rate(%)'])
        lis.append(fig)

    fig1 = go.Figure(lis);
    fig1.update_xaxes(tickvals=df_purbam.index, ticktext=df_purbam['Year'])
    fig1.update_layout(title=f'Dropout Analysis on All Caste : ', xaxis_title='Year', yaxis_title='Dropout Rate')
    return fig1;

def getList(df):
    lis = df['Cast'].unique().tolist()
    return lis;

def getdf():
    df = pd.read_csv('Datasets/Cast.csv')
    return df;
