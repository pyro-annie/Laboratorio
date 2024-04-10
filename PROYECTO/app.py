from flask import Flask, request, jsonify, render_template
import re
import secrets
import string

app = Flask(__name__)

users = {}

password_requirements = {
    'uppercase': 1,
    'digits': 1,
    'special': 1,
    'min_length': 8
}

def check_password_requirements(password):
    patterns = {
        'uppercase': r'[A-Z]',
        'digits': r'\d',
        'special': r'\W'
    }
    return all(len(re.findall(pattern, password)) >= password_requirements[requirement]
               for requirement, pattern in patterns.items()) and len(password) >= password_requirements['min_length']

def generate_secure_password():
    alphabet = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(password_requirements['min_length']))
        if check_password_requirements(password):
            break
    return password

@app.route('/generate-password', methods=['POST'])
def generate_password():
    return jsonify({'password': generate_secure_password()})

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name'].strip()
    password = request.form['password']

    if name in users:
        return jsonify({'error': 'El nombre de usuario ya está en uso. Por favor, elige otro.'}), 400

    if not check_password_requirements(password):
        return jsonify({'error': 'La contraseña no cumple con los requisitos necesarios. Asegúrate de que tenga al menos 8 caracteres, incluyendo mayúsculas, minúsculas, caracteres especiales y números.'}), 400

    users[name] = {'password': password}
    return jsonify({'message': 'Usuario registrado con éxito.'})

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username'].strip()
    password = request.form['password']

    if username not in users:
        return jsonify({'error': 'El nombre de usuario no está registrado. Por favor, verifica tus datos o regístrate.'}), 400

    if users[username]['password'] != password:
        return jsonify({'error': 'La contraseña introducida es incorrecta. Por favor, inténtalo de nuevo.'}), 400

    return jsonify({'message': f'Bienvenido, {username}'})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)   