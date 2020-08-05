import dash
import requests
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import constants as C
from app import app


TITLE_STYLE = C.TITLE_STYLE


@app.callback(
    [dash.dependencies.Output('session', 'data')],
    [dash.dependencies.Input('donut1', 'clickData')])
def updateOn(clickData):
    try:
        print(f'point number is {clickData["points"][0]["pointNumber"]}')
        return [{'point': clickData['points'][0]['pointNumber']}]
    except:
        return [{'point': '0'}]


@app.callback(
    [dash.dependencies.Output('graph1', 'figure')],
    [dash.dependencies.Input('session', 'data')])
def updateSession(data):
    try:
        print(data)
        if data['point'] == 4 or data['point'] == 6:
            url = C.SURVIVED_DATA
            titleId = '2'
        elif data['point'] == 3 or data['point'] == 5:
            url = C.DIED_DATA
            titleId = '1'
        else:
            url = C.AGE_DATA
            titleId = '0'
    except:
        url = C.AGE_DATA
    print(url)
    # Get the data, if api not reachable prevent update
    try:
        ageData = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(e)
        raise dash.exceptions.PreventUpdate
    TITLE_STYLE['text'] = '<b>Age vs Count<b>'
    barPlot = go.Figure(
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
            xaxis_title="<b>Age Range<b>",
            yaxis_title=C.YAXIS_TITLE[0][titleId],
            legend_title="Gender",
            margin={
                'b': 0
            }
        )
    ),
    return barPlot


@app.callback([
    dash.dependencies.Output('graph3', 'figure'),
    dash.dependencies.Output('graph2', 'figure')],
    [dash.dependencies.Input('graph1', 'clickData'),
     dash.dependencies.Input('session', 'data')])
def updateOnBarClick(clickValue, data):
    """ Generate figure based on click event data

    Args:
        clickValue (dict): Data from latest click event

    Raises:
        dash.exceptions.PreventUpdate: Prevent updates when API is not reachable

    Returns:
        Figure : Plotly Figure Object
    """
    try:
        print(clickValue)
        isFemale = clickValue['points'][0]['curveNumber']
        ageRange = clickValue['points'][0]['x']
    except TypeError:
        isFemale = 0
        ageRange = '0-5'
    print(isFemale, ageRange, data)
    if isFemale:
        apiUrl = C.API_BASE_URL + "/fare/" + \
            ageRange + "/1/" + str(data['point'])
    else:
        apiUrl = C.API_BASE_URL + "/fare/" + \
            ageRange + "/0/" + str(data['point'])
    print(apiUrl)

    # Get the data, if api not reachable prevent update
    try:
        response = requests.get(apiUrl)
    except requests.exceptions.RequestException as e:
        print(e)
        raise dash.exceptions.PreventUpdate

    TITLE_STYLE['text'] = '<b>Fare Distribution<b>'
    scatterPlot = go.Figure(
        data=[go.Scatter(
            x=response.json()['x'],
            y=response.json()['y'],
            mode='markers',
            marker={'size': 10}
            # TODO: Marker color based on Pclass
            # marker_color=response.json()['color']
            # marker={'color': response.json()['color'], 'colorscale':[
            #    [0, 'rgb(0,0,255)'], [1, 'rgb(255,0,0)']]}
        )],
        layout=go.Layout(
            title=TITLE_STYLE,
            font=C.FONT_STYLE,
            xaxis_title="<b>Passanger ID<b>",
            yaxis_title="<b>Fare<b>"

        )
    )

    TITLE_STYLE['text'] = '<b>Passanger Class Distribution<b>'
    piePlot = go.Figure(
        data=[go.Pie(
            labels=response.json()['labels'],
            values=response.json()['values']
        )],
        layout=go.Layout(
            title=TITLE_STYLE,
            font=C.FONT_STYLE,
            legend_title="Passanger Class",
        )
    )
    return piePlot, scatterPlot
