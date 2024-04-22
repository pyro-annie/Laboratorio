# txtcrud.py
import os

# Ruta de la carpeta donde se guardarán los archivos txt
folder_path = 'databasetxt'

# Crear la carpeta si no existe
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

def guardar_evento(evento):
    file_path = os.path.join(folder_path, 'eventos.txt')
    with open(file_path, 'a') as file:
        file.write(f"{evento['nombre']},{evento['descripcion']},{evento['ubicacion']},{evento['fecha']},{evento['horario_inicio']},{evento['horario_fin']}\n")

def guardar_participante(participante):
    file_path = os.path.join(folder_path, 'participantes.txt')
    with open(file_path, 'a') as file:
        file.write(f"{participante['nombre']},{participante['contacto']},{participante['preferencias_alimenticias']},{participante['asistencia']}\n")

def obtener_eventos():
    eventos = []
    file_path = os.path.join(folder_path, 'eventos.txt')
    try:
        with open(file_path, 'r') as file:
            for linea in file:
                nombre, descripcion, ubicacion, fecha, horario_inicio, horario_fin = linea.strip().split(',')
                eventos.append({
                    'nombre': nombre,
                    'descripcion': descripcion,
                    'ubicacion': ubicacion,
                    'fecha': fecha,
                    'horario_inicio': horario_inicio,
                    'horario_fin': horario_fin
                })
    except FileNotFoundError:
        pass
    return eventos

def obtener_participantes():
    participantes = []
    file_path = os.path.join(folder_path, 'participantes.txt')
    try:
        with open(file_path, 'r') as file:
            for linea in file:
                nombre, contacto, preferencias_alimenticias, asistencia = linea.strip().split(',')
                participantes.append({
                    'nombre': nombre,
                    'contacto': contacto,
                    'preferencias_alimenticias': preferencias_alimenticias,
                    'asistencia': asistencia
                })
    except FileNotFoundError:
        pass
    return participantes
