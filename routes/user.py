from flask import Blueprint, g, escape, session, redirect, render_template, request, jsonify, Response, flash
from app import Dao
from util import *

from controllers.user_manager import UserManager

user_view = Blueprint('user_routes', __name__, template_folder="/templates")
user_manager = UserManager()

@user_view.route('/', methods=['GET'])
def home():
    g.bg = 1
    user_manager.user.set_session(session, g)
    print(g.user)
    
    return render_template('home.html', g=g)

@user_view.route('/login', methods=['get', 'post'])
@user_manager.user.redirect_if_login
def login():
    if request.method == 'POST':
        _form = request.form
        email = str(_form['email'])
        password = str(_form['password'])
        
        if len(email) < 1 or len(password) < 1:
            return render_template('login.html', error="email and password are required")
        
        d = user_manager.login(email, hash(password))
        
        if d and len(d) > 0:
            session['user'] = int(d['id'])
            
            return redirect['/']
        
        return render_template('login.html', error="email and password are incorrect")
    return render_template('login.html')

@user_view.route('/register', methods=['GET', 'POST'])
@user_manager.user.redirect_if_login
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if len(name) < 1 or len(email) < 1 or len(password) < 1:
            return render_template('register.html', error="all fields are required")
        
        new_user = user_manager.add_user(name, email, hash(password))
        
        if new_user == "already exists":
            return render_template('register.html', error="user already exists with this email")
        return render_template('register.html', msg="you've b een registered successfully")
    return render_template('register.html')

@user_view.route('/logout/', methods=['GET'])
@user_manager.user.login_required
def logout():
    user_manager.logout()
    return redirect('/', code=302)

@user_view.route('/user/', methods=['GET'])
@user_manager.user.login_required
def show_user(id=None):
    user_manager.user.set_session(session, g)
    
    if id is None:
        id = int(user_manager.user.uid())
        
    d = user_manager.get(id)
    books = user_manager.get_book_list(id)
    
    return render_template('profile.html', user=d, books=books, g=g)

@user_view.route('/user', methods=['POST'])
@user_manager.user.login_required
def update():
    user_manager.user.set_session(session, g)
    _form = request.form
    name = str(_form['name'])
    email = str(_form['email'])
    password = str(_form['password'])
    bio =  str(_form['bio'])
    
    user_manager.update(name, email, hash(password), bio, user_manager.user.uid())
    
    flash('you info has been updated')
    
    return redirect('/user')
        