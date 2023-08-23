import os
import pandas as pd

# Paso 1: Especificar la ruta donde se encuentran los archivos CSV
ruta_base = '/home/ak/Escritorio/Pyt/log'

# Paso 2: Crear una lista para almacenar los DataFrames de cada archivo CSV
dataframes_list = []

# Paso 3: Recorrer cada subcarpeta y archivo CSV en la ruta base
for root, _, files in os.walk(ruta_base):
    for file in files:
        if file.endswith('.csv'):
            archivo_csv = os.path.join(root, file)
            # Paso 4: Leer el archivo CSV
            data = pd.read_csv(archivo_csv)
            # Paso 5: Agregar el DataFrame a la lista
            dataframes_list.append(data)

# Paso 6: Concatenar todos los DataFrames en uno solo
all_data = pd.concat(dataframes_list)

# Paso 7: Agrupar los datos por "SerialNumber"
grouped_data = all_data.groupby('serialNumber')

# Paso 8: Crear una lista para almacenar los DataFrames de cada grupo
grouped_data_list = []

# Paso 9: Recorrer cada grupo y agregarlo a la lista
for serial_number, group in grouped_data:
    grouped_data_list.append(group)

# Paso 10: Concatenar nuevamente los DataFrames para tener todos los datos agrupados en uno solo
grouped_data_concatenated = pd.concat(grouped_data_list)

# Paso 11: Ordenar las filas en función de los datos de la columna "location|timeStamp"
sorted_data = grouped_data_concatenated.sort_values(by='location|timeStamp')

# Paso 12: Exportar los datos agrupados a un nuevo archivo CSV
output_file = '/home/ak/Escritorio/Pyt/Exports/archivo_agrupado.csv'
pd.concat(grouped_data_list).to_csv(output_file, index=False)

print("Datos agrupados exportados exitosamente a:", output_file)

# Paso 13: Recorrer cada grupo y guardar los datos en archivos CSV separados
for serial_number, group in grouped_data:
    # Crear un nombre de archivo único basado en el serialNumber
    output_file = f'/home/ak/Escritorio/Pyt/Exports/{serial_number}.csv'
    # Guardar los datos del grupo en el archivo CSV
    group.to_csv(output_file, index=False)

print("Archivos CSV, según número de serie, creados y guardados exitosamente.")

