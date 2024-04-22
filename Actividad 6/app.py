# app.py
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from txtcrud import guardar_evento, guardar_participante, obtener_eventos, obtener_participantes

app = Flask(__name__)

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

@app.route('/agregar_evento', methods=['GET', 'POST'])
def agregar_evento():
    if request.method == 'POST':
        evento = {
            'nombre': request.form['nombre'],
            'descripcion': request.form['descripcion'],
            'ubicacion': request.form['ubicacion'],
            'fecha': request.form['fecha'],
            'horario_inicio': request.form['horario_inicio'],
            'horario_fin': request.form['horario_fin']
        }
        guardar_evento(evento)
        return redirect(url_for('mostrar_eventos'))
    return render_template('agregar_evento.html')

@app.route('/agregar_participante', methods=['GET', 'POST'])
def agregar_participante():
    if request.method == 'POST':
        participante = {
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
    # Aquí iría la lógica para mostrar la interfaz de modificación/eliminación de participantes
    return 'Interfaz de modificación/eliminación de participantes'

@app.route('/modificar_eventos')
def modificar_eventos():
    # Aquí iría la lógica para mostrar la interfaz de modificación/eliminación de eventos
    return 'Interfaz de modificación/eliminación de eventos'

if __name__ == '__main__':
    app.run(debug=True)
