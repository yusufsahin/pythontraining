import configparser

# configparser nesnesi oluştur
config = configparser.ConfigParser()

# settings.ini dosyasını oku
config.read('settings.ini')

# Değerleri al ve yazdır
database_host = config['database']['host']
database_port = config['database']['port']
server_host = config['server']['host']
server_port = config['server']['port']
logging_level = config['logging']['level']
logging_file = config['logging']['file']

print(f"Database host: {database_host}")
print(f"Database port: {database_port}")
print(f"Server host: {server_host}")
print(f"Server port: {server_port}")
print(f"Logging level: {logging_level}")
print(f"Logging file: {logging_file}")
