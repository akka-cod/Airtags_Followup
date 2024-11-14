# Airtags Followup

--------------------------------------------------------------------

*Español*

**Recursos**:
- Script de almacenamiento de ubicaciones: [https://github.com/fjxmlzn/FindMyHistory]
- Script de síntesis y órden de datos: [https://github.com/akka-cod/CSV_works/blob/main/Clean_CSVs.py]
- Script de sincronización de datos y mapeo: Databay
- Tmux: [Github - Tmux](https://github.com/tmux/tmux/wiki)
- Crontab: Crontab Guru - [https://crontab.guru/]

**Instrucciones para ejecutar el seguimiento**:
- **Sistema**:
    - Full access disk de Terminal
        - Ajustes > Privacidad > Acceso total al disco > Añadir terminal
    - Sincronización con iCloud: Total
    - Tras ejecutar "Find My History" en paso 5 - Activar crontab para ejecución automática del Script de Sincronización de datos.
        - Abrimos terminal
        - contrab -u usuario	[usuario es nombre del usuario]
        - Agregaremos las tareas al archivo creado, desde la ventana que se habrá abierto al ejecutar el comando anterior.
            - Ej: 0 10 * * * /ruta/al/script	[esto ejecutará el script de la ruta cada día de cada mes a las 10:00 am]
    - Activar Tmux para activación de procesos de terminal en segundo plano. [opcional]
- **Buscar o Find My**:
    - Abrimos la aplicación y la dejamos corriendo “ad infinitum”
    - La información de esta aplicación la podemos encontrar en la ruta: 
        - Finder > Ir > Pulsamos “Alt” para mostrar opciones ocultas > Biblioteca > Caches > com.apple.findmy.fmipcore
        - La información que vemos aquí es la información de los airtags que será extraída por el primer script para ser almacenada en archivos csv.
- **Find My History**:
    - Este es un script descargado y ejecutado localmente, que extrae los datos de la ruta antes mencionada y los almacena en nuevos archivos csv.
    - Instrucciones de descarga y ejecución: https://github.com/fjxmlzn/FindMyHistory
    - Al seguir las instrucciones anteriores, el script quedará ejecutándose y almacenando la información de la siguiente manera:
        - En la carpeta del script: “ordenador” > “Macintosh HD” > "User" > FindMyHistory > log
        - Aquí tendremos una carpeta por cada día de registro
            - Dentro, tendremos un archivo csv por cada dispositivo con nuevas ubicaciones.
- **Sincronización de datos y mapeo**:
    - En principio, se programará la ejecución del Script de sincronización de datos para cada día subir al servidor los datos del día anterior.
    - Databay se encarga del mapeo y crear la interfaz de visualización de las ubicaciones.
- **Tratamiento de datos en servidor**:
    - En caso de necesitar la síntesis y ordenado de múltiples archivos csv de múltiples dispositivos y de múltiples días, disponemos del Script de síntesis y órden de datos: [https://github.com/akka-cod/CSV_works/blob/main/Clean_CSVs.py]

--------------------------------------------------------------------

*English*

**Resources**:
- Location Storage Script: [https://github.com/fjxmlzn/FindMyHistory]
- Data Synthesis and Sorting Script: [https://github.com/akka-cod/CSV_works/blob/main/Clean_CSVs.py]
- Data Synchronization Script and Mapping: Databay
- Tmux: [Github - Tmux](https://github.com/tmux/tmux/wiki)
- Crontab: Crontab Guru - [https://crontab.guru/]

**Instructions for running the trace**:
- **System**:
    - Full access disk for Terminal
        - Settings > Privacy > Full Disk Access > Add terminal
    - iCloud Sync: Total
    - Enable crontab for automatic execution of the Data Synchronization Script.
        - Open terminal
        - contrab -u user	[user is the exactly name of the current user]
        - We will add the tasks to the created file, from the window that will have opened when executing the previous command.
            - Ex: 0 10 * * * /route/to/script	[This will run the route script every day of every month at 10:00 am]
    - Enable Tmux for background terminal process activation. [optional]
- **Find o Find My**:
    - We open the app and let it run "ad infinitum"
    - The information of this application can be found on the route: 
        - Finder > Go > Press "Alt" to show hidden options > Library > Caches > com.apple.findmy.fmipcore
        - The information we see here is the information from the airtags that will be extracted by the first script to be stored in csv files.
- **Find My History**:
    - This is a script downloaded and executed locally, which extracts the data from the aforementioned path and stores it in new csv files.
    - Download & run instructions: https://github.com/fjxmlzn/FindMyHistory
    - By following the instructions above, the script will be running and storing the information as follows:
        - In the script folder: “Computer” > “Macintosh HD” > "User" > FindMyHistory > log
        - Here we will have a folder for each day of registration
            - Inside, we will have a csv file for each device with new locations.
- **Data synchronization and Mapping**:
    - In principle, the execution of the Data Synchronization Script will be scheduled for each day to upload the previous day's data to the server.
    - Databay takes care of the mapping and creating the visualization interface of the locations.
- **Server-side data processing**:
    - In case you need the synthesis and sorting of multiple csv files from multiple devices and multiple days, we have the Synthesis and Data Order Script: [https://github.com/akka-cod/CSV_works/blob/main/Clean_CSVs.py]
 
