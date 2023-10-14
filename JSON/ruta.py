import json

# Ruta al archivo JSON
json_file_path = 'JSON/railway.json'

# Abre y carga el archivo JSON
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)

# Ahora, 'data' contiene el contenido del archivo JSON
print(data)
