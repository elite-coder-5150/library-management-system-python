from flask import Blueprint, g, escape, session, redirect, render_template, request, jsonify, Response, flash
from app import Dao

from controllers.admin_manager import AdminManager
from controllers.book_manager import BookManager
from controllers.user_manager import UserManager

av = Blueprint('admin_routes', __name__, template_folder='../template/admin/routes', url_prefix='admin_routes')

bm = BookManager(Dao)
um = UserManager(Dao)
am = AdminManager(Dao)

@av.route('/', methods=['GET'])
@am.admin.login_required
def home():
    am.admin.set_session(session, g)
    return render_template('admin/home.html', g=g)

@av.route('/admin/login', methods=['GET', 'POST'])
@am.admin.redirect_if_login
def login():
    g.bg = 1
    
    if request.method == 'POST':
        _form = request.form
        email = str(_form['email'])
        password = str(_form['password'])
        
        if len(email) < 1 or len(password) < 1:
            return render_template('admin/login.html', error="email and password are required")
        
        d = am.login(email, hash(password))
        
        if d and len(d) > 0:
            session['admin'] = int(d['id'])
            return redirect('/admin');
        return render_template('admin/login.html', error="email and password are incorrect")
    return render_template('admin/login.html')

@av.route('/logout/', methods=['GET'])
@am.admin.login_required
def logout():
    am.logout()
    return redirect('/admin', code= 302)

@av.route('/users/view', methods=['GET'])
@am.admin.login_required
def users_view():
    am.admin.set_session(session)
    id = int(am.admin.uid())
    admin = am.get(id)
    users = am.get_users_list()
    
    return render_template('users.html', g=g, admin=admin, users=users)


@av.route('/books/', methods=['GET'])
@am.admin.login_required
def books():
    am.admin.set_session(session, g)