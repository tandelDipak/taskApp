import dash
import requests
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import constants as C
from app import app


TITLE_STYLE = C.TITLE_STYLE


@app.callback([
    dash.dependencies.Output('graph3', 'figure'),
    dash.dependencies.Output('graph2', 'figure')],
    [dash.dependencies.Input('graph1', 'clickData')])
def updateOnClick(clickValue):
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
    print(isFemale, ageRange)
    if isFemale:
        apiUrl = C.API_BASE_URL + "graph2/" + ageRange + "/1"
    else:
        apiUrl = C.API_BASE_URL + "graph2/" + ageRange + "/0"
    print(apiUrl)

    # Get the data, if api not reachable prevent update
    try:
        response = requests.get(apiUrl)
    except requests.exceptions.RequestException as e:
        print(e)
        raise dash.exceptions.PreventUpdate

    TITLE_STYLE['text'] = 'Fare Distribution'
    scatterPlot = go.Figure(
        data=[go.Scatter(
            x=response.json()['x'],
            y=response.json()['y'],
            mode='markers',
            # TODO: Marker color based on Pclass
            # marker_color=response.json()['color']
            # marker={'color': response.json()['color'], 'colorscale':[
            #    [0, 'rgb(0,0,255)'], [1, 'rgb(255,0,0)']]}
        )],
        layout=go.Layout(
            title=TITLE_STYLE,
            font=C.FONT_STYLE,
            xaxis_title="Passanger ID",
            yaxis_title="Fare"

        )
    )

    TITLE_STYLE['text'] = 'Passanger Class Distribution'
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
