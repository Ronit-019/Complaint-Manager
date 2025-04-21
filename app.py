from flask import Flask,render_template, request, redirect, session
from db import Database
import os

app = Flask(__name__)
app.secret_key = "your_secret_key_here"
dbo = Database()

UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = {'png','jpg','jpeg','gif'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/complaint')
def complaint():
    return render_template('complaint.html')

@app.route('/perform_registration',methods=['post'])
def perform_registration():
    name = request.form.get("user_name")
    email = request.form.get("user_email")
    password = request.form.get("password")
    response = dbo.insert(name,email,password)

    if response:
        return render_template('login.html',message="Registration Successful. Kindly Login to Proceed")
    else:
        return render_template('register.html',message="Email Already Exists")

@app.route('/perform_login', methods=['post'])
def perform_login():
    email = request.form.get("user_email")
    password = request.form.get("password")
    response = dbo.search(email, password)

    if response:
        session['logged_in'] = 1
        return redirect('/complaint')
    else:
        return render_template('login.html', message="Incorrect Email/Password")

@app.route('/perform_complaint', methods=['post'])
def perform_complaint():
    email = request.form.get("user_email")
    title = request.form.get("c_title")
    desc = request.form.get("c_desc")
    categ = request.form.get("category")
    loc = request.form.get("location")
    photo = request.files.get("photo")

    photo_filename = None

    if photo:
        photo_filename = os.path.join(UPLOAD_FOLDER,photo.filename)
        photo.save(photo_filename)
    else:
        photo_filename = None

    dat = request.form.get("date")
    urg = request.form.get("urgency")

    response = dbo.insertco(email,title,desc,categ,loc,dat,photo_filename,urg)

    if response == 1:
        return render_template("complaint.html",message="Complaint Submitted Successfully")
    else:
        return render_template('complaint.html', message="User Email does not exist")

app.run(debug=True)