import dash
import os
from layouts import layout1
import config


environment = os.environ['CONF_ENV']
if environment == 'production':
    print("Production Configuration")
    appConfig = config.ProductionConfig()
elif environment == 'development':
    print("Development Configuration")
    appConfig = config.DevelopmentConfig()
elif environment == 'testing':
    print("Testing Configuration")
    appConfig = config.TestingConfig()
elif environment == 'jenkinsDevelopment':
    print("Jenkins Development Configuration")
    appConfig = config.JenkinsDevelopmentConfig()
elif environment == 'jenkinsTesting':
    print("Jenkins Testing Configuration")
    appConfig == config.JenkinsTestingConfig()
else:
    appConfig = config.config()
    print("Default Configuration")


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.layout = layout1
if __name__ == '__main__':
    app.run_server(port=appConfig.APP_PORT, debug=appConfig.DEBUG)
