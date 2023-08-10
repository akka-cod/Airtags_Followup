import os
import pandas as pd
import folium

# Paso 1: Especificar la ruta donde se encuentran los archivos CSV
ruta_base = '/home/ak/Escritorio/Pyt/Exports'

# Paso 2: Crear una lista para almacenar los DataFrames de cada archivo CSV
dataframes_list = []

# Paso 3: Recorrer cada archivo CSV en la ruta base y leerlo en un DataFrame
for root, _, files in os.walk(ruta_base):
    for file in files:
        if file.endswith('.csv'):
            archivo_csv = os.path.join(root, file)
            data = pd.read_csv(archivo_csv)
            dataframes_list.append(data)

# Paso 4: Concatenar todos los DataFrames en uno solo
all_data = pd.concat(dataframes_list)

# Paso 5: Crear un mapa usando folium
mapa = folium.Map(location=[all_data['location|latitude'].mean(), all_data['location|longitude'].mean()], zoom_start=15)

# Paso 6: Agregar una trayectoria al mapa
trayectoria = folium.PolyLine(locations=all_data[['location|latitude', 'location|longitude']].values.tolist(), color='blue')
trayectoria.add_to(mapa)

# Paso 7: Guardar el mapa como un archivo HTML interactivo
mapa.save('/home/ak/Escritorio/Pyt/Exports/Maps/trayectoria_mapa.html')

print("Mapa de trayectoria generado y guardado exitosamente.")
