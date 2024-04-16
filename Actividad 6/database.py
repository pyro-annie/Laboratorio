# Modelo de conexión para Excel usando pandas
import pandas as pd

class ExcelConexion:
    def __init__(self, archivo):
        self.archivo = archivo

    def leer_datos(self):
        return pd.read_excel(self.archivo)

    def insertar_datos(self, datos):
        datos.to_excel(self.archivo, index=False)

    def actualizar_datos(self, datos_actualizados):
        datos_actualizados.to_excel(self.archivo, index=False)

    def eliminar_datos(self, condicion):
        datos = pd.read_excel(self.archivo)
        datos_filtrados = datos[~condicion]
        datos_filtrados.to_excel(self.archivo, index=False)

# Modelo de conexión para MySQL usando pymysql
import pymysql

class MySQLConexion:
    def __init__(self, host, usuario, contraseña, base_datos):
        self.conexion = pymysql.connect(host=host, user=usuario, password=contraseña, db=base_datos)

    def leer_datos(self, consulta):
        with self.conexion.cursor() as cursor:
            cursor.execute(consulta)
            return cursor.fetchall()

    def insertar_datos(self, consulta):
        with self.conexion.cursor() as cursor:
            cursor.execute(consulta)
            self.conexion.commit()

    def actualizar_datos(self, consulta):
        with self.conexion.cursor() as cursor:
            cursor.execute(consulta)
            self.conexion.commit()

    def eliminar_datos(self, consulta):
        with self.conexion.cursor() as cursor:
            cursor.execute(consulta)
            self.conexion.commit()

# Modelo de conexión para Access usando pyodbc
import pyodbc

class AccessConexion:
    def __init__(self, ruta_archivo):
        self.conexion = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + ruta_archivo)

    def leer_datos(self, consulta):
        with self.conexion.cursor() as cursor:
            cursor.execute(consulta)
            return cursor.fetchall()

    def insertar_datos(self, consulta):
        with self.conexion.cursor() as cursor:
            cursor.execute(consulta)
            self.conexion.commit()

    def actualizar_datos(self, consulta):
        with self.conexion.cursor() as cursor:
            cursor.execute(consulta)
            self.conexion.commit()

    def eliminar_datos(self, consulta):
        with self.conexion.cursor() as cursor:
            cursor.execute(consulta)
            self.conexion.commit()

# Modelo de conexión para archivos de texto
class TxtConexion:
    def __init__(self, archivo):
        self.archivo = archivo

    def leer_datos(self):
        with open(self.archivo, 'r') as file:
            return file.readlines()

    def insertar_datos(self, datos):
        with open(self.archivo, 'a') as file:
            file.write(datos + '\n')

    def actualizar_datos(self, datos_actualizados):
        with open(self.archivo, 'w') as file:
            file.writelines(datos_actualizados)

    def eliminar_datos(self, condicion):
        with open(self.archivo, 'r') as file:
            lineas = file.readlines()
        with open(self.archivo, 'w') as file:
            for linea in lineas:
                if not condicion(linea):
                    file.write(linea)
