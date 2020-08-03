import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import requests
import constants as C

try:
    ageData = requests.get(C.AGE_DATA)
    barData = requests.get(C.BAR_DATA)
except requests.exceptions.RequestException as e:
    raise SystemExit(e)

layout1 = html.Div(children=[
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
