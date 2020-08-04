import os
from app import app
from layouts import layout1
import config
import callbacks

environment = os.environ.get('CONF_ENV', 'default')
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

app.layout = layout1

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=appConfig.APP_PORT,
                   debug=appConfig.DEBUG)
