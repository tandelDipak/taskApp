#!/usr/bin/env python
# coding: utf-8

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import plotly.graph_objs as go
import requests


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


url = 'http://0.0.0.0:5005/api/v1/resources/'
g1 = url + 'graph1'
g2 = url + 'graph2/0-5/0'
g3 = url + 'graph3'


try:
    response = requests.get(g1)
    response2 = requests.get(g2)
except ConnectionRefusedError:
    pass


app.layout = html.Div(children=[
    dcc.Graph(
        id='graph1',
        figure=go.Figure(
            data=[go.Bar(
                name='Male',
                x=response.json()['male']['x'],
                y=response.json()['male']['y']
            ),
                go.Bar(
                name='Female',
                x=response.json()['female']['x'],
                y=response.json()['female']['y'],
            )],
            layout=go.Layout(
                title="Graph One"
            )
        )
    ),
    html.Div([
        html.Div([
            dcc.Graph(
                id='graph2',
                figure=go.Figure(
                    data=[go.Scatter(
                        x=response2.json()['x'],
                        y=response2.json()['y'],
                        mode='markers',
                        # marker={'color': response2.json(
                        # )['color'], 'colorscale':'Viridis'}
                    )],
                    layout=go.Layout(
                        title="Call durations",

                    )
                )
            )
        ], className="six columns"),
        html.Div([
            dcc.Graph(
                id='graph3',
                figure=go.Figure(
                    data=[go.Pie(
                        labels=response2.json()['labels'],
                        values=response2.json()['values']
                    )],
                    layout=go.Layout(
                        title="Cause Code"
                    )
                )
            )
        ], className="six columns")
    ], className="row")
])


@app.callback([
    dash.dependencies.Output('graph3', 'figure'),
    dash.dependencies.Output('graph2', 'figure')],
    [dash.dependencies.Input('graph1', 'clickData')])
def updateOnClick(clickValue):
    try:
        print(clickValue)
        isFemale = clickValue['points'][0]['curveNumber']
        ageRange = clickValue['points'][0]['x']
    except TypeError:
        isFemale = 0
        ageRange = '0-5'
    print(isFemale, ageRange)
    if isFemale:
        apiUrl = url + "graph2/" + ageRange + "/1"
    else:
        apiUrl = url + "graph2/" + ageRange + "/0"
    print(apiUrl)
    response = requests.get(apiUrl)
    scatterPlot = go.Figure(
        data=[go.Scatter(
            x=response.json()['x'],
            y=response.json()['y'],
            mode='markers',
            # marker={'color': response.json()['color'], 'colorscale':[
            #    [0, 'rgb(0,0,255)'], [1, 'rgb(255,0,0)']]}
        )],
        layout=go.Layout(
            title="Call durations",

        )
    )
    piePlot = go.Figure(
        data=[go.Pie(
            labels=response.json()['labels'],
            values=response.json()['values']
        )],
        layout=go.Layout(
            title="Cause Code"
        )
    )
    temp = type(scatterPlot)
    if temp == None:
        print("Its None")
    else:
        print("Else")
    return piePlot, scatterPlot


if __name__ == '__main__':
    app.run_server(port=8060, debug=True)
