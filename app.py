import mysql.connector
from pathlib import Path
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from dotenv import load_dotenv
from db_formatter import db_formatter
from time import sleep
import os
import shutil
from flask import Flask, flash, request, redirect, render_template, url_for, session
from werkzeug.utils import secure_filename

print("Starting...")
database_check = False
while not database_check:
    print("Checking Database Integrity...")

    if db_formatter(True):
        print("MySQL Database Check Verified!")
        print("Starting Server Soon")
        sleep(0.1)
        database_check = True
    else:
        print("MySQL Database Check Failed! Please reset the Database")
        print("Restarting Check in 5 Seconds")
        sleep(5)
        database_check = False

env_path = Path('.', '.env')
load_dotenv(dotenv_path=env_path)

db_host = os.getenv('MYSQL_DATABASE_HOST')
db_user = os.getenv('MYSQL_DATABASE_USERNAME')
db_pass = os.getenv('MYSQL_DATABASE_PASSWORD')
db_db = os.getenv('MYSQL_DATABASE_DATABASE')

VID_UPLOAD_FOLDER = './vid'
FONT_UPLOAD_FOLDER = './font'
CSS_UPLOAD_FOLDER = './css'
JS_UPLOAD_FOLDER = './js'
GIF_UPLOAD_FOLDER = './gif'
IMG_UPLOAD_FOLDER = './img'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'css', 'js', 'jpeg', 'woff', 'woff2', 'otf', 'ttf', 'mp4', 'mp4', 'wmv', 'wov', 'gif', 'webp', 'svg'}

app = Flask(__name__)
app.run(debug=True)

app.config['GIF_UPLOAD_FOLDER'] = GIF_UPLOAD_FOLDER
app.config['JS_UPLOAD_FOLDER'] = JS_UPLOAD_FOLDER
app.config['CSS_UPLOAD_FOLDER'] = CSS_UPLOAD_FOLDER
app.config['FONT_UPLOAD_FOLDER'] = FONT_UPLOAD_FOLDER
app.config['VID_UPLOAD_FOLDER'] = VID_UPLOAD_FOLDER
app.config['IMG_UPLOAD_FOLDER'] = IMG_UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.secret_key = 'sijuygv8rvng8ofg48fgh'

app.config['MYSQL_HOST'] = db_host
app.config['MYSQL_USER'] = db_user
app.config['MYSQL_PASSWORD'] = db_pass
app.config['MYSQL_DB'] = db_db

mysql = MySQL(app)


@app.route('/')
def home():
    return redirect(url_for('upload'))


@app.route('/cdn-admin/login/', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE email = %s AND password = %s', (email, password,))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['email'] = account['email']
            # Redirect to home page
            return redirect(url_for('upload'))
        else:
            msg = 'Incorrect email/password!'
    return render_template('login.html', msg=msg)


@app.route('/cdn-admin/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('email', None)
    return redirect(url_for('login'))


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/cdn-admin/upload/', methods=['GET', 'POST'])
def upload():
    msg = ''
    global filename
    global row_id
    if 'loggedin' in session:
        if request.method == 'POST':
            action_upload = request.form['action_upload']
            action_filename = request.form['action_filename']
            action_file_format = request.form['action_file_format']
            if 'files[]' not in request.files:
                flash('No file part')
                return redirect(request.url)
            files = request.files.getlist('files[]')
            for file in files:
                if file and allowed_file(file.filename):
                    if action_upload == 'img':
                        filename = secure_filename(file.filename)
                        file.save(os.path.join(app.config['IMG_UPLOAD_FOLDER'], filename))
                        image_rename_old = os.path.join(app.config['IMG_UPLOAD_FOLDER'], filename)
                        image_rename_new = os.path.join(app.config['IMG_UPLOAD_FOLDER'],
                                                        f"{action_filename}.{action_file_format}")
                        shutil.move(image_rename_old, image_rename_new)
                    if action_upload == 'css':
                        filename = secure_filename(file.filename)
                        file.save(os.path.join(app.config['CSS_UPLOAD_FOLDER'], filename))
                        image_rename_old = os.path.join(app.config['CSS_UPLOAD_FOLDER'], filename)
                        image_rename_new = os.path.join(app.config['CSS_UPLOAD_FOLDER'],
                                                        f"{action_filename}.css")
                        shutil.move(image_rename_old, image_rename_new)

                    if action_upload == 'vid':
                        filename = secure_filename(file.filename)
                        file.save(os.path.join(app.config['CSS_UPLOAD_FOLDER'], filename))
                        image_rename_old = os.path.join(app.config['CSS_UPLOAD_FOLDER'], filename)
                        image_rename_new = os.path.join(app.config['CSS_UPLOAD_FOLDER'],
                                                        f"{action_filename}.{action_file_format}")
                        shutil.move(image_rename_old, image_rename_new)

                    if action_upload == 'font':
                        filename = secure_filename(file.filename)
                        file.save(os.path.join(app.config['CSS_UPLOAD_FOLDER'], filename))
                        image_rename_old = os.path.join(app.config['CSS_UPLOAD_FOLDER'], filename)
                        image_rename_new = os.path.join(app.config['CSS_UPLOAD_FOLDER'],
                                                        f"{action_filename}.{action_file_format}")
                        shutil.move(image_rename_old, image_rename_new)

                    if action_upload == 'gif':
                        filename = secure_filename(file.filename)
                        file.save(os.path.join(app.config['CSS_UPLOAD_FOLDER'], filename))
                        image_rename_old = os.path.join(app.config['CSS_UPLOAD_FOLDER'], filename)
                        image_rename_new = os.path.join(app.config['CSS_UPLOAD_FOLDER'],
                                                        f"{action_filename}.gif")
                        shutil.move(image_rename_old, image_rename_new)

                    if action_upload == 'js':
                        filename = secure_filename(file.filename)
                        file.save(os.path.join(app.config['CSS_UPLOAD_FOLDER'], filename))
                        image_rename_old = os.path.join(app.config['CSS_UPLOAD_FOLDER'], filename)
                        image_rename_new = os.path.join(app.config['CSS_UPLOAD_FOLDER'],
                                                        f"{action_filename}.js")
                        shutil.move(image_rename_old, image_rename_new)

            flash('File(s) successfully uploaded')
            return redirect(url_for('upload'))

        return render_template('upload.html')
    return redirect(url_for('login'))