# txtcrud.py
import os
import uuid

# Ruta de la carpeta donde se guardarán los archivos txt
folder_path = 'databasetxt'

# Crear la carpeta si no existe
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

def guardar_evento(evento):
    file_path = os.path.join(folder_path, 'eventos.txt')
    with open(file_path, 'a') as file:
        file.write(f"{evento['id']},{evento['nombre']},{evento['descripcion']},{evento['ubicacion']},{evento['fecha']},{evento['horario_inicio']},{evento['horario_fin']}\n")
        
def guardar_participante(participante):
    file_path = os.path.join(folder_path, 'participantes.txt')
    with open(file_path, 'a') as file:
        file.write(f"{participante['id']},{participante['nombre']},{participante['contacto']},{participante['preferencias_alimenticias']},{participante['asistencia']}\n")
        
# Función para actualizar un evento existente
def actualizar_evento(evento_actualizado, id_evento):
    eventos = obtener_eventos()
    # Encontrar y actualizar el evento por ID
    for i, evento in enumerate(eventos):
        if evento['id'] == id_evento:
            eventos[i] = evento_actualizado
            break
    # Guardar los eventos actualizados en el archivo
    with open(os.path.join(folder_path, 'eventos.txt'), 'w') as file:
        for evento in eventos:
            file.write(f"{evento['nombre']},{evento['descripcion']},{evento['ubicacion']},{evento['fecha']},{evento['horario_inicio']},{evento['horario_fin']}\n")

# Función para eliminar un evento por ID
def eliminar_evento(id_evento):
    eventos = obtener_eventos()
    # Eliminar el evento por ID
    eventos = [evento for evento in eventos if evento['id'] != id_evento]
    # Guardar los eventos restantes en el archivo
    with open(os.path.join(folder_path, 'eventos.txt'), 'w') as file:
        for evento in eventos:
            file.write(f"{evento['nombre']},{evento['descripcion']},{evento['ubicacion']},{evento['fecha']},{evento['horario_inicio']},{evento['horario_fin']}\n")

# Función para obtener todos los eventos con ID
def obtener_eventos():
    eventos = []
    file_path = os.path.join(folder_path, 'eventos.txt')
    try:
        with open(file_path, 'r') as file:
            for linea in file:
                nombre, descripcion, ubicacion, fecha, horario_inicio, horario_fin = linea.strip().split(',')
                eventos.append({
                    'id': len(eventos) + 1,  # Asignar un ID único a cada evento
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
                id, nombre, contacto, preferencias_alimenticias, asistencia = linea.strip().split(',')
                participantes.append({
                    'id': id,
                    'nombre': nombre,
                    'contacto': contacto,
                    'preferencias_alimenticias': preferencias_alimenticias,
                    'asistencia': asistencia == 'True'
                })
    except FileNotFoundError:
        pass
    return participantes

# Función para generar un ID único para los participantes
def generar_id_unico():
    return str(uuid.uuid4())
# Ejemplo de uso de la función generar_id_unico
nuevo_id = generar_id_unico()
