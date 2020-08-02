import dash
from layouts import layout1
import callbacks
#import dash_core_components as dcc
#import dash_html_components as html
#import plotly.express as px
#import pandas as pd
#import plotly.graph_objs as go
#import constants as C
#from layouts import layout1


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.layout = layout1
if __name__ == '__main__':
    app.run_server(port=8060, debug=True)
