import mysql.connector as db
import csv

mydb = db.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'mysql123',
    database = 'ayudantia_1'
)

cursor = mydb.cursor()

tabla_sucursales = ''' CREATE TABLE sucursales(
    id_sucursal INT PRIMARY KEY,
    direccion VARCHAR(255),
    comuna VARCHAR(255)
)'''

#cursor.execute(tabla_sucursales)

tabla_empleados = '''CREATE TABLE empleados (
    rut INT PRIMARY KEY,
    nombre VARCHAR(255),
    edad INT,
    cargo VARCHAR(255),
    sueldo INT, 
    id_sucursal INT, FOREIGN KEY (id_sucursal) REFERENCES sucursales(id_sucursal)
    )'''


#cursor.execute(tabla_empleados)

# poblar tabla sucursales

with open('data/sucursales.csv') as file:
    csvreader = csv.reader(file, delimiter = ';')
    next(csvreader)
    filas = []
    for fila in csvreader:
        filas.append(fila)

insertar_sucursales = '''INSERT INTO sucursales (id_sucursal, direccion, comuna) VALUES (%s, %s, %s)'''
cursor.executemany(insertar_sucursales, filas)
#with open('data/sucursales.csv') as file:
    #csvreader = csv.reader(file, delimiter=';')
    #next(csvreader)
    #filas = []
    #for fila in csvreader:
        #filas.append(fila)
#insertar_sucursales = '''INSERT INTO sucursales (id_sucursal, direccion, comuna) VALUES (%s, %s, %s)'''
# cursor.executemany(insertar_sucursales, filas)

# poblar tabla empleados
#with open('data/empleados.csv') as file:
    #csvreader = csv.reader(file, delimiter=';')
    #next(csvreader)
    #filas = []
    #for fila in csvreader:
        #filas.append(fila)
#insertar_empleados = '''INSERT INTO empleados (rut, nombre, edad, cargo, sueldo, id_sucursal) VALUES (%s, %s, %s, %s, %s, %s)'''
#cursor.executemany(insertar_empleados, filas)

mydb.commit()

