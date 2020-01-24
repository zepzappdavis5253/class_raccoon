
######################### Lab01 Password Generator ######################################
from flask import Flask, render_template, request, redirect

import random
import string
import urllib
import json

app = Flask(__name__)

def generate_password(n):
    alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password = ''.join([random.choice(alphabet) for i in range(n)])
    return password

def load_database():
    with open('database.json', 'r') as file:
        data = json.loads(file.read())
    return data

def save_database(data):
    with open('database.json', 'w') as file:
        file.write(json.dumps(data))





@app.route('/')
def index():
    return render_template('index.html')

@app.route('/password_generator/', methods=['GET', 'POST'])
def password_generator():

    data = load_database()
    password = ''
    if request.method == 'POST':
        password_length = int(request.form['password_length'])
        password = generate_password(password_length)

        data['pass'].append({'password': password})

        save_database(data)

    return render_template('password_generator.html', password_result=password)



@app.route('/oneview/', methods=['GET', 'POST'])
def oneview():
    if request.method == 'POST':

        if request.form['form_type'] == 'random_password':
            password_length = int(request.form['password_length'])
            password = generate_password(password_length)
            return render_template('oneview.html', password_result=password)
        else:
            input_text = request.form['input_text']
            rot_amount = int(request.form['rot_amount'])
            alphabet = string.ascii_lowercase
            output = ''
            for char in input_text:
                index = alphabet.find(char)
                if index == -1:
                    output += char
                else:
                    output += alphabet[(index+rot_amount)%len(alphabet)]
            return render_template('oneview.html', rot13_result=output)

        print(request.form)
    return render_template('oneview.html')


@app.route('/multiview/', methods=['GET'])
def multiview():
    data = load_database()
    password = data['password']
    data['password'] = ''
    save_database(data)
    return render_template('multiview.html', password_result=password)

@app.route('/multiview_password_generator/', methods=['POST'])
def multiview_password_generator():
    password_length = int(request.form['password_length'])
    password = generate_password(password_length)
    print(password)
    data = load_database()
    data['password'] = password
    save_database(data)
    # return render_template('multiview.html', password_result=password)
    return redirect('/multiview/')

##################################################################################################################
