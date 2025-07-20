from flask import Blueprint, render_template, request, redirect, url_for, session
from app.db import get_connection
from app.models.model import query

projectManagers_bp = Blueprint('projectManagers', __name__, url_prefix='/projectManagers')

@projectManagers_bp.route('/')
def home():
    if 'user_id' not in session:
        return redirect(url_for('main.login'))

    if session['role_id'] == 1:
        return redirect(url_for('admin.home'))
    elif session['role_id'] == 3:
        return redirect(url_for('teamMember.home'))
    
    projects = query("""
        select id, start_date, deadline, title, description, progress
        from projects
        where manager_id = %s
    """,(session['user_id'],))

    users = query("""
        select name
        from users
        where availability = 'available'
        """)

    return render_template('projectManagers_pages/pm_home.html', projects=projects, users=users)

@projectManagers_bp.route('/task', methods=['POST'])
def assignTask():

    description = request.form['taskDesc']
    assigned_to = request.form['assignedTo']
    priority = request.form['priority']
    deadline = request.form['deadline']
    comments = request.form['comments']
    project_id = request.form['projectId']

    query("""
        insert into tasks 
        (description, assigned_to, priority, deadline, comments, project_id, progress)
        values (%s,%s,%s,%s,%s,%s,'todo')
        """,(description, assigned_to, priority, deadline, comments, project_id))
    
    redirect('projectManagers.home')

@projectManagers_bp.route('/profile/')
def profile():

    if 'user_id' not in session:
        return redirect(url_for('main.login'))

    if session['role_id'] == 1:
        return redirect(url_for('admin.home'))
    elif session['role_id'] == 3:
        return redirect(url_for('teamMember.home'))

    profile = query("""
        select u.id, u.name, u.email, r.title
        from users u
        join roles r
        on u.role_id = r.id 
        where u.id = %s
    """,(session['user_id'],))[0]

    return render_template('projectManagers_pages/pm_profile.html', profile=profile)