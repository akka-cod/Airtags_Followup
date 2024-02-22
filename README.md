# CSV_works

**Recursos**:
- Script de almacenamiento de ubicaciones: https://github.com/fjxmlzn/FindMyHistory
- Script de síntesis y órden de datos: https://github.com/akka-cod/CSV_works/blob/main/Clean_CSVs.py
- Script de sincronización de datos:
- Tmux: [Github - Tmux](https://github.com/tmux/tmux/wiki)
- Crontab: Crontab Guru - https://crontab.guru/

**Instrucciones para ejecutar el seguimiento**:
- **Sistema**:
    - Full access disk de Terminal
        - Ajustes > Privacidad > Acceso total al disco > Añadir terminal
    - Sincronización con iCloud: Total
    - Activar crontab para ejecución automática del Script de Sincronización de datos.
        - Abrimos terminal
        - contrab -u usuario	[usuario es nombre del usuario]
        - Agregaremos las tareas al archivo creado, desde la ventana que se habrá abierto al ejecutar el comando anterior.
            - Ej: 0 10 * * * /ruta/al/script	[esto ejecutará el script de la ruta cada día de cada mes a las 10:00 am]
    - Activar Tmux para activación de procesos de terminal en segundo plano. [opcional]
- **Buscar o Find My**:
    - Abrimos la aplicación y la dejamos corriendo “ad infinitum”
    - La información de esta aplicación la podemos encontrar en la ruta: 
        - Finder > Ir > Pulsamos “Alt” para mostrar opciones ocultas > Biblioteca > Caches > com.apple.findmy.fmipcore
        - La información que vemos aquí es la información de los airbags que será extraída por el primer script para ser almacenada en archivos csv.
- **Find My History**:
    - Este es un script descargado y ejecutado localmente, que extrae los datos de la ruta antes mencionada y los almacena en nuevos archivos csv.
    - Instrucciones de descarga y ejecución: https://github.com/fjxmlzn/FindMyHistory
    - Al seguir las instrucciones anteriores, el script quedará ejecutándose y almacenando la información de la siguiente manera:
        - En la carpeta del script: “ordenador” > “Macintosh HD” > Bofh > FindMyHistory > log
        - Aquí tendremos una carpeta por cada día de registro
            - Dentro, tendremos un archivo csv por cada dispositivo con nuevas ubicaciones.
- **Sincronización de datos**:
    - En principio, se programará la ejecución del Script de sincronización de datos para cada día subir al servidor los datos del día anterior.
- **Tratamiento de datos en servidor**:
    - En caso de necesitar la síntesis y ordenado de múltiples archivos csv de múltiples dispositivos y de múltiples días, disponemos del Script de síntesis y órden de datos: https://github.com/akka-cod/CSV_works/blob/main/Clean_CSVs.py
