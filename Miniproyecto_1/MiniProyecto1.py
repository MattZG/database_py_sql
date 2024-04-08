#Importado del modulo para hacer la conexion

import mysql.connector as db

#Creacion la conexion con el motor

mydb = db.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'mysql123',
    database = 'infoaeropuertos'
)

#Creacion del cursor

cursor = mydb.cursor()

#Instruccion en SQL para agregar informacion a la tabla

sqlsentence = 'INSERT INTO aeropuertos(id, ident, type, name, elevation_ft, municipality, iata_code, score) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'

#Carga de los datos a agregar

filas = [
    (39340, 'SHCC', 'heliport', 'Clinica Las Condes Heliport', 2461, 'Santiago', None, 25),
    (39379, 'SHMA', 'heliport', 'Clinica Santa Maria Heliport', 2028, 'Santiago', None, 25),
    (39390, 'SHPT', 'heliport', 'Portillo Heliport', 9000, 'Los Andes', None, 25)
]

#Agregacion de los datos a la tabla

cursor.executemany(sqlsentence, filas)
mydb.commit()

#Definicion de la consulta

consulta = 'SELECT name, type, municipality, elevation_ft FROM aeropuertos WHERE elevation_ft > 5000'

#Ejecucion de la consulta

cursor.execute(consulta)

#Obtencion de los resultados

resultados = cursor.fetchall()

#Impresion de los resultados

for fila in resultados:
    print(fila)

print('El total de aerpuertos que cumplen con esta condicion son: ', len(resultados))