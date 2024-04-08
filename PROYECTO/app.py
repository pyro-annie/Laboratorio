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
    has_uppercase = len(re.findall(r'[A-Z]', password)) >= password_requirements['uppercase']
    has_digit = len(re.findall(r'\d', password)) >= password_requirements['digits']
    has_special = len(re.findall(r'\W', password)) >= password_requirements['special']
    is_long_enough = len(password) >= password_requirements['min_length']
    return has_uppercase and has_digit and has_special and is_long_enough

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
    name = request.form['name']
    password = request.form['password']

    if not check_password_requirements(password):
        return jsonify({'error': 'La contraseña debe tener al menos 8 caracteres, incluyendo mayúsculas, minúsculas, caracter especiales y números.'}), 400

    if name in users:
        return jsonify({'error': 'El usuario ya existe'}), 400

    users[name] = {'password': password}
    return jsonify({'message': 'Usuario registrado con éxito'})

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username not in users:
        return jsonify({'error': 'Usuario no registrado'}), 400

    if users[username]['password'] != password:
        return jsonify({'error': 'Contraseña errónea, intente otra vez'}), 400

    return jsonify({'message': 'Bienvenido, ' + username})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)