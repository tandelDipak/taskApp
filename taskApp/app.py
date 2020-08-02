#!/usr/bin/env python
# coding: utf-8


import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import plotly.graph_objs as go
import requests
import constants as C


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


try:
    ageData = requests.get(C.AGE_DATA)
    barData = requests.get(C.BAR_DATA)
except ConnectionRefusedError:
    pass


app.layout = html.Div(children=[
    dcc.Graph(
        id='graph1',
        figure=go.Figure(
            data=[go.Bar(
                name='Male',
                x=ageData.json()['male']['x'],
                y=ageData.json()['male']['y']
            ),
                go.Bar(
                name='Female',
                x=ageData.json()['female']['x'],
                y=ageData.json()['female']['y'],
            )],
            layout=go.Layout(
                title=C.TITLE_STYLE,
                font=C.FONT_STYLE,
                xaxis_title="Age Range",
                yaxis_title="Passanger Count",
                legend_title="Gender"
            )
        )
    ),
    html.Div([
        html.Div([
            dcc.Graph(
                id='graph2',
                figure=go.Figure(
                    data=[go.Scatter(
                        x=barData.json()['x'],
                        y=barData.json()['y'],
                        mode='markers',
                        # marker_color=response2.json()['color']
                        # marker={'color': response2.json(
                        # )['color'], 'colorscale':'Viridis'}
                    )],
                    layout=go.Layout(
                        title="Fare Distribution",
                        xaxis_title="Passanger ID",
                        yaxis_title="Fare"

                    )
                )
            )
        ], className="six columns"),
        html.Div([
            dcc.Graph(
                id='graph3',
                figure=go.Figure(
                    data=[go.Pie(
                        labels=barData.json()['labels'],
                        values=barData.json()['values']
                    )],
                    layout=go.Layout(
                        title="Passanger Class Distribution",
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
        apiUrl = C.API_BASE_URL + "graph2/" + ageRange + "/1"
    else:
        apiUrl = C.API_BASE_URL + "graph2/" + ageRange + "/0"
    print(apiUrl)
    response = requests.get(apiUrl)
    scatterPlot = go.Figure(
        data=[go.Scatter(
            x=response.json()['x'],
            y=response.json()['y'],
            mode='markers',
            # marker_color=response.json()['color']
            # marker={'color': response.json()['color'], 'colorscale':[
            #    [0, 'rgb(0,0,255)'], [1, 'rgb(255,0,0)']]}
        )],
        layout=go.Layout(
            title=C.TITLE_STYLE,
            font=C.FONT_STYLE,
            xaxis_title="Passanger ID",
            yaxis_title="Fare"

        )
    )
    piePlot = go.Figure(
        data=[go.Pie(
            labels=response.json()['labels'],
            values=response.json()['values']
        )],
        layout=go.Layout(
            title=C.TITLE_STYLE,
            font=C.FONT_STYLE,
            legend_title="Passanger Class",
        )
    )

    return piePlot, scatterPlot


if __name__ == '__main__':
    app.run_server(port=8060, debug=True)
