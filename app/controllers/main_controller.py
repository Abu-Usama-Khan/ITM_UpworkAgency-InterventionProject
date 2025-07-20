from flask import Blueprint, render_template, request, redirect, url_for, session
from app.models.model import query

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    session.clear
    if 'user_id' in session:    
        if session['role_id'] == 1:
            return redirect(url_for('admin.home'))
        elif session['role_id'] == 2:
            return redirect(url_for('projectManagers.home'))
        else:
            return redirect(url_for('teamMembers.home'))
    return render_template('login.html')

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = query("SELECT id, role_id FROM users WHERE email = %s AND password = %s", (email, password))[0]

        if user:
            session['user_id'] = user[0]
            session['role_id'] = user[1]
            if session['role_id'] == 1:
                return redirect(url_for('admin.home'))
            elif session['role_id'] == 2:
                return redirect(url_for('projectManagers.home'))
            else:
                return redirect(url_for('teamMembers.home'))
        else:
            return render_template('login.html', error="Invalid credentials.")
    return render_template('login.html')

@main_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.home'))