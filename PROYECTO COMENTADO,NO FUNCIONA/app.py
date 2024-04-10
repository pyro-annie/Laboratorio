from flask import Flask, request, jsonify, render_template 
# Importamos las librerías necesarias para la aplicación web. el archivo por defecto debe llamarse app.apy 
# para que funcione,si quieres cambiar el nombre,lo tienes que aclarar en el cmd
import re  # Librería para trabajar con expresiones regulares.
import secrets  # Librería para generar contraseñas seguras.
import string  # Librería que contiene secuencias de caracteres comunes.

# Creamos una instancia de la aplicación Flask.
app = Flask(__name__)

# Inicializamos un diccionario para almacenar los usuarios y sus contraseñas.
users = {}

# Establecemos los requisitos que debe cumplir una contraseña.
password_requirements = {
    'uppercase': 1,  # Al menos 1 letra mayúscula.
    'digits': 1,     # Al menos 1 dígito.
    'special': 1,    # Al menos 1 carácter especial.
    'min_length': 8  # Longitud mínima de 8 caracteres.
}

# Definimos una función para verificar si una contraseña cumple con los requisitos.
def check_password_requirements(password):
    # Patrones para buscar en la contraseña.
    patterns = {
        'uppercase': r'[A-Z]',  # Busca letras mayúsculas.
        'digits': r'\d',        # Busca dígitos.
        'special': r'\W'        # Busca caracteres especiales.
    }
    # Verifica que la contraseña cumpla con cada requisito y tenga la longitud mínima.
    return all(len(re.findall(pattern, password)) >= password_requirements[requirement]
               for requirement, pattern in patterns.items()) and len(password) >= password_requirements['min_length']

# Definimos una función para generar una contraseña segura.
def generate_secure_password():
    # Creamos un alfabeto con letras, dígitos y puntuación.
    alphabet = string.ascii_letters + string.digits + string.punctuation
    while True:
        # Generamos una contraseña aleatoria.
        password = ''.join(secrets.choice(alphabet) for i in range(password_requirements['min_length']))
        # Verificamos si la contraseña cumple con los requisitos.
        if check_password_requirements(password):
            break
    return password

# Ruta para generar una contraseña segura.
@app.route('/generate-password', methods=['POST'])
def generate_password():
    return jsonify({'password': generate_secure_password()})

# Ruta para registrar un nuevo usuario.
@app.route('/register', methods=['POST'])
def register():
    # Obtenemos el nombre y la contraseña del formulario.
    name = request.form['name'].strip()
    password = request.form['password']

    # Verificamos si el nombre de usuario ya existe.
    if name in users:
        return jsonify({'error': 'El nombre de usuario ya está en uso. Por favor, elige otro.'}), 400

    # Verificamos si la contraseña cumple con los requisitos.
    if not check_password_requirements(password):
        return jsonify({'error': 'La contraseña no cumple con los requisitos necesarios. Asegúrate de que tenga al menos 8 caracteres, incluyendo mayúsculas, minúsculas, caracteres especiales y números.'}), 400

    # Registramos al usuario.
    users[name] = {'password': password}
    return jsonify({'message': 'Usuario registrado con éxito.'})

# Ruta para iniciar sesión.
@app.route('/login', methods=['POST'])
def login():
    # Obtenemos el nombre de usuario y la contraseña del formulario.
    username = request.form['username'].strip()
    password = request.form['password']

    # Verificamos si el nombre de usuario está registrado.
    if username not in users:
        return jsonify({'error': 'El nombre de usuario no está registrado. Por favor, verifica tus datos o regístrate.'}), 400

    # Verificamos si la contraseña es correcta.
    if users[username]['password'] != password:
        return jsonify({'error': 'La contraseña introducida es incorrecta. Por favor, inténtalo de nuevo.'}), 400

    # Si todo es correcto, damos la bienvenida al usuario.
    return jsonify({'message': f'Bienvenido, {username}'})

# Ruta principal que muestra la página de inicio.
@app.route('/')
def index():
    return render_template('index.html')

# Verificamos si este archivo es el archivo principal y ejecutamos la aplicación.
if __name__ == '__main__':
    app.run(debug=True)