import configparser

config = configparser.ConfigParser()

config['database'] = {
    'host': 'localhost',
    'port': '5432',
    'username': 'admin',
    'password': 'secret'
}

config['server'] = {
    'host': '0.0.0.0',
    'port': '8000'
}

config['logging'] = {
    'level': 'INFO',
    'file': 'app.log'
}

with open('settings.ini', 'w') as configfile:
    config.write(configfile)