from flaskproject import app, db
from flask import request, session, url_for, make_response
from flask.json import jsonify
from flask.templating import render_template
from werkzeug.utils import redirect
import hashlib
from flaskproject.models import UserDetails, Admins
from datetime import datetime, timedelta
import jwt
from flaskproject.decorator import token_required

@app.route('/')
def home():
    users = UserDetails.query.all()
    return render_template('index.html',users = users)

@app.route('/register', methods= ["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        hashedPassword = hashlib.md5(bytes(str(password),encoding='utf-8'))
        hashedPassword = hashedPassword.hexdigest() 

        # register the new user to the database
        new_user = UserDetails(username = username, email = email, password = hashedPassword)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template("register.html")

@app.route('/login', methods=["POST","GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        hashedPassword = hashlib.md5(bytes(str(password),encoding='utf-8'))
        hashedPassword = hashedPassword.hexdigest()
        result = UserDetails.query.filter_by(username = username).first()
        if result == None or hashedPassword != result.password:
            return "Invalid email or password"
        token = jwt.encode({'user':result.email, 'exp': datetime.utcnow()+timedelta(minutes=15)}, app.config['SECRET_KEY'])
        session["jwt"] = token
        return redirect(url_for('dashboard'))
    return render_template("login.html")

@app.route('/dashboard')
@token_required
def dashboard(current_user):
    return render_template('dashboard.html', data=current_user)

@app.route('/admin_dashboard')
@token_required
def admin_dashboard(current_user):
    return render_template('admin_dashboard.html')

@app.route('/admin', methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        result = Admins.query.filter_by(username = username).first()
        if result == None or password != result.password:
            return "Invalid email or password"
        token = jwt.encode({'user':result.email, 'exp': datetime.utcnow()+timedelta(minutes=15)}, app.config['SECRET_KEY'])
        session["jwt"] = token
        return redirect(url_for('admin_dashboard'))
    return render_template("admin_login.html")