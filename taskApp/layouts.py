import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import requests
import constants as C

try:
    ageData = requests.get(C.AGE_DATA)
    barData = requests.get(C.BAR_DATA)
    summaryData = requests.get(C.SUMMARY)
except requests.exceptions.RequestException as e:
    raise SystemExit(e)

layout1 = html.Div(children=[
    dcc.Store(id='memory'),
    dcc.Graph(
        id='donut1',
        figure=go.Figure(
            data=[go.Sunburst(
                labels=summaryData.json()['labels'][0],
                parents=summaryData.json()['parents'],
                values=summaryData.json()['values'],
                branchvalues="total"
            )],
            layout=go.Layout(
                title=C.SUMMARY_TITLE,
                font=C.FONT_STYLE,
                margin={
                    'b': 0
                }
            ),
        ),
        config={
            'displayModeBar': False
        }
    ),
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
                xaxis_title="<b>Age Range<b>",
                yaxis_title="<b>Passanger Count<b>",
                legend_title="Gender",
                margin={
                    'b': 0
                }
            )
        ),
        config={
            'displayModeBar': False
        }
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
                ),
                config={
                    'displayModeBar': False
                }
            ),
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
                ),
                config={
                    'displayModeBar': False
                }
            )
        ], className="six columns")
    ], className="row")
])
