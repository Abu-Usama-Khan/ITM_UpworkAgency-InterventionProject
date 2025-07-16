from flask import Blueprint, render_template, request, redirect, url_for, session
from app.db import get_connection

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    if 'user_id' in session:
        return redirect(url_for('main.dashboard'))
    return render_template('login.html')

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT id, role_id FROM users WHERE email = %s AND password = %s", (email, password))
        user = cursor.fetchone()
        cursor.close()
        connection.close()

        if user:
            session['user_id'] = user[0]
            session['role_id'] = user[1]
            return redirect(url_for('main.dashboard'))
        else:
            return render_template('login.html', error="Invalid credentials.")
    return render_template('login.html')

@main_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.home'))

@main_bp.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('main.login'))

    user_id = session['user_id']
    role_id = session['role_id']

    connection = get_connection()
    cursor = connection.cursor()

    if role_id == 1:
        cursor.execute("""
            SELECT p.id, p.name, COUNT(t.id) as task_count
            FROM projects p
            LEFT JOIN tasks t ON p.id = t.project_id
            GROUP BY p.id
        """)
    elif role_id == 2:
        cursor.execute("""
            SELECT p.id, p.name, COUNT(t.id) as task_count
            FROM projects p
            LEFT JOIN tasks t ON p.id = t.project_id
            WHERE p.manager_id = %s
            GROUP BY p.id
        """, (user_id,))
    else:
        cursor.execute("""
            SELECT DISTINCT p.id, p.name
            FROM projects p
            JOIN tasks t ON p.id = t.project_id
            WHERE t.assigned_to = %s
        """, (user_id,))

    projects = cursor.fetchall()
    cursor.close()
    connection.close()

    return render_template('dashboard.html', projects=projects, role_id=role_id)

@main_bp.route('/project/<int:project_id>')
def view_project(project_id):
    if 'user_id' not in session:
        return redirect(url_for('main.login'))

    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT title, status, assigned_to FROM tasks WHERE project_id = %s", (project_id,))
    tasks = cursor.fetchall()

    cursor.execute("SELECT name FROM projects WHERE id = %s", (project_id,))
    project = cursor.fetchone()

    cursor.close()
    connection.close()

    return render_template('project_detail.html', project=project, tasks=tasks)
