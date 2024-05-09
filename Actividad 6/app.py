# app.py
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from txtcrud import guardar_evento, guardar_participante, obtener_eventos, obtener_participantes
import uuid

app = Flask(__name__)
# Función para actualizar un evento existente
def actualizar_evento(evento_actualizado, id_evento):
    eventos = obtener_eventos()
    # Encontrar y actualizar el evento por ID
    for i, evento in enumerate(eventos):
        if evento['id'] == id_evento:
            eventos[i] = evento_actualizado
            break
    # Guardar los eventos actualizados en el archivo
    with open('databasetxt/eventos.txt', 'w') as file:
        for evento in eventos:
            file.write(f"{evento['nombre']},{evento['descripcion']},{evento['ubicacion']},{evento['fecha']},{evento['horario_inicio']},{evento['horario_fin']}\n")
            

# Función para eliminar un evento por ID
def eliminar_evento_por_id(id_evento):
    eventos = obtener_eventos()
    # Eliminar el evento por ID
    eventos = [evento for evento in eventos if evento['id'] != id_evento]
    # Guardar los eventos restantes en el archivo
    with open('databasetxt/eventos.txt', 'w') as file:
        for evento in eventos:
            file.write(f"{evento['nombre']},{evento['descripcion']},{evento['ubicacion']},{evento['fecha']},{evento['horario_inicio']},{evento['horario_fin']}\n")

def editar_evento(id_evento):
    eventos = obtener_eventos()  # Obtener la lista de eventos
    evento = next((e for e in eventos if e['id'] == id_evento), None)
    if not evento:
        return "Evento no encontrado"

    if request.method == 'POST':
        # Código para actualizar el evento
        evento['nombre'] = request.form['nombre']
        evento['descripcion'] = request.form['descripcion']
        evento['ubicacion'] = request.form['ubicacion']
        evento['fecha'] = request.form['fecha']
        evento['horario_inicio'] = request.form['horario_inicio']
        evento['horario_fin'] = request.form['horario_fin']

        # Guardar los cambios en el archivo eventos.txt
        with open('databasetxt/eventos.txt', 'w') as file:
            for e in eventos:
                if e['id'] == id_evento:
                    file.write(f"{evento['nombre']},{evento['descripcion']},{evento['ubicacion']},{evento['fecha']},{evento['horario_inicio']},{evento['horario_fin']}\n")
                else:
                    file.write(f"{e['nombre']},{e['descripcion']},{e['ubicacion']},{e['fecha']},{e['horario_inicio']},{e['horario_fin']}\n")

        return redirect(url_for('modificar_eventos'))

    return render_template('editar_evento.html', evento=evento)

def actualizar_participante(participante_actualizado, id_participante):
    participantes = obtener_participantes()
    # Encontrar y actualizar el participante por ID
    for i, participante in enumerate(participantes):
        if participante['id'] == id_participante:
            participantes[i] = participante_actualizado
            break
    # Guardar los participantes actualizados en el archivo
    with open(os.path.join(folder_path, 'participantes.txt'), 'w') as file:
        for participante in participantes:
            file.write(f"{participante['nombre']},{participante['contacto']},{participante['preferencias_alimenticias']},{participante['asistencia']}\n")



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/eventos')
def mostrar_eventos():
    eventos = obtener_eventos()
    return render_template('eventos.html', eventos=eventos)

@app.route('/participantes')
def mostrar_participantes():
    participantes = obtener_participantes()
    return render_template('participantes.html', participantes=participantes)

import uuid

@app.route('/agregar_participante', methods=['GET', 'POST'])
def agregar_participante():
    if request.method == 'POST':
        # Genera un ID único para el nuevo participante
        nuevo_id = str(uuid.uuid4())
        participante = {
            'id': nuevo_id,
            'nombre': request.form['nombre'],
            'contacto': request.form['contacto'],
            'preferencias_alimenticias': request.form['preferencias_alimenticias'],
            'asistencia': 'asistencia' in request.form
        }
        guardar_participante(participante)
        return redirect(url_for('mostrar_participantes'))
    return render_template('newparticipante.html')


@app.route('/modificar_participantes')
def modificar_participantes():
    participantes = obtener_participantes()  # Asegúrate de tener esta función definida
    return render_template('modificar_participantes.html', participantes=participantes)

# Función para actualizar un participante existente
@app.route('/editar_participante/<int:id>', methods=['GET', 'POST'])
def editar_participante(id):
    participantes = obtener_participantes()  # Obtener la lista de participantes
    participante = next((p for p in participantes if p['id'] == id), None)
    if not participante:
        return "Participante no encontrado", 404

    if request.method == 'POST':
        # Código para actualizar el participante
        participante['nombre'] = request.form['nombre']
        participante['contacto'] = request.form['contacto']
        participante['preferencias_alimenticias'] = request.form['preferencias_alimenticias']
        participante['asistencia'] = 'asistencia' in request.form
        # Guardar los cambios en el archivo participantes.txt
        actualizar_participante(participante, id)
        return redirect(url_for('mostrar_participantes'))

    return render_template('editar_participante.html', participante=participante)


# Función para eliminar un participante por ID
@app.route('/eliminar_participante/<int:id>', methods=['POST'])
def eliminar_participante(id):
    participantes = obtener_participantes()  # Obtener la lista de participantes
    # Encontrar el índice del participante a eliminar
    participante_a_eliminar = next((i for i, p in enumerate(participantes) if p['id'] == id), None)
    # Si se encuentra el participante, eliminarlo de la lista
    if participante_a_eliminar is not None:
        participantes.pop(participante_a_eliminar)
    # Guardar la lista actualizada en el archivo participantes.txt
    with open('databasetxt/participantes.txt', 'w') as file:
        for p in participantes:
            file.write(f"{p['nombre']},{p['contacto']},{p['preferencias_alimenticias']},{p['asistencia']}\n")

    return redirect(url_for('mostrar_participantes'))


@app.route('/modificar_eventos')
def modificar_eventos():
    # Código para mostrar la lista de eventos con opciones para editar o eliminar
    eventos = obtener_eventos()
    return render_template('modificar_eventos.html', eventos=eventos)

@app.route('/editar_evento/<int:id>', methods=['GET', 'POST'])
def editar_evento(id):
    eventos = obtener_eventos()  # Obtener la lista de eventos
    evento = next((e for e in eventos if e['id'] == id), None)
    if not evento:
        return "Evento no encontrado", 404

    if request.method == 'POST':
        # Código para actualizar el evento
        evento['nombre'] = request.form['nombre']
        evento['descripcion'] = request.form['descripcion']
        evento['ubicacion'] = request.form['ubicacion']
        evento['fecha'] = request.form['fecha']
        evento['horario_inicio'] = request.form['horario_inicio']
        evento['horario_fin'] = request.form['horario_fin']
        # Guardar los cambios en el archivo eventos.txt
        actualizar_evento(evento, id)
        return redirect(url_for('modificar_eventos'))

    return render_template('editar_evento.html', evento=evento)

@app.route('/eliminar_evento/<int:id>', methods=['POST'])
def eliminar_evento(id):
    eventos = obtener_eventos()  # Obtener la lista de eventos
    # Encontrar el índice del evento a eliminar
    evento_a_eliminar = next((i for i, e in enumerate(eventos) if e['id'] == id), None)
    # Si se encuentra el evento, eliminarlo de la lista
    if evento_a_eliminar is not None:
        eventos.pop(evento_a_eliminar)
    # Guardar la lista actualizada en el archivo eventos.txt
    with open('databasetxt/eventos.txt', 'w') as file:
        for e in eventos:
            file.write(f"{e['nombre']},{e['descripcion']},{e['ubicacion']},{e['fecha']},{e['horario_inicio']},{e['horario_fin']}\n")

    return redirect(url_for('modificar_eventos'))
@app.route('/eliminar_evento/<int:id>', methods=['POST'])
def eliminar_evento_por_id(id):
    eventos = obtener_eventos()  # Obtener la lista de eventos
    evento = next((e for e in eventos if e['id'] == id), None)
    if not evento:
        return "Evento no encontrado", 404

    # Eliminar el evento de la lista
    evento.remove(evento)
    # Guardar la lista actualizada en el archivo eventos.txt
    with open('databasetxt/eventos.txt', 'w') as file:
        for e in eventos:
            file.write(f"{e['nombre']},{e['descripcion']},{e['ubicacion']},{e['fecha']},{e['horario_inicio']},{e['horario_fin']}\n")

    return redirect(url_for('modificar_eventos'))

# Asegúrate de definir las funciones obtener_eventos, actualizar_evento y las demás funciones necesarias.

# Ruta para mostrar la página newevents.html
@app.route('/newevents')
def new_events():
    return render_template('newevents.html')

# Ruta para manejar el formulario enviado desde newevents.html
@app.route('/agregar_evento', methods=['GET', 'POST'])
def agregar_evento():
    if request.method == 'POST':
        # Lógica para manejar los datos del formulario enviado
        nombre = request.form.get('nombre')
        descripcion = request.form.get('descripcion')
        ubicacion = request.form.get('ubicacion')
        fecha = request.form.get('fecha')
        horario_inicio = request.form.get('horario_inicio')
        horario_fin = request.form.get('horario_fin')

        evento = {
            'nombre': nombre,
            'descripcion': descripcion,
            'ubicacion': ubicacion,
            'fecha': fecha,
            'horario_inicio': horario_inicio,
            'horario_fin': horario_fin
        }
        guardar_evento(evento)

        # Redirige al usuario a la página principal
        return redirect('/')
    else:
        # Si el método es GET, muestra la página para agregar un nuevo evento
        return render_template('newevents.html')

if __name__ == '__main__':
    app.run(debug=True)