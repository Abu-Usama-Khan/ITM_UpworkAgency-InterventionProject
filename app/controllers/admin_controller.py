from flask import Blueprint, render_template, request, redirect, url_for, session
from app.db import get_connection

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/')
def home():
    if 'user_id' not in session:
        return redirect(url_for('main.login'))

    if session['role_id'] == 2:
        return redirect(url_for('projectManagers.home'))
    elif session['role_id'] == 3:
        return redirect(url_for('teamMembers.home'))

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        select id, title, description
        from projects
        where manager_id is null
    """)

    projects = cursor.fetchall()

    cursor.execute("""
        select name
        from users
        where role_id=2
    """)

    project_mgrs = cursor.fetchall()

    cursor.execute("""
        select id, title, job_description, proposal, feasibility
        from job_proposal 
        where status = 'active'
    """)

    active_jobs = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('admin_pages/admin_home.html', 
                           projects=projects, project_mgrs=project_mgrs, active_jobs=active_jobs)

@admin_bp.route('/project/', methods=['POST']) 
def assignProject():
    project_id = request.form['project_id']
    start_date = request.form['start_date']
    deadline = request.form['deadline']
    manager_name = request.form['manager_name']
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        select id from users where name = %s
        """,(manager_name,))
    
    manager_id = cursor.fetchone()[0]              

    cursor.execute("""
        UPDATE projects
        SET start_date = %s,
        deadline = %s,
        manager_id = %s,
        progress = 0
        WHERE id = %s
        """, (start_date, deadline, manager_id, project_id))

    connection.commit()

    cursor.close()
    connection.close()
    
    return redirect(url_for('admin.home'))

@admin_bp.route('/job/', methods=['POST']) 
def approveJob():
    job_id = request.form['job_id']
    approval = request.form['approval']
    connection = get_connection()
    cursor = connection.cursor()          

    cursor.execute("""
        UPDATE job_proposal
        SET status = 'inactive',
        approval = %s
        WHERE id = %s
        """, (approval, job_id))

    connection.commit()

    cursor.execute("""
        select title, job_description
        from job_proposal
        WHERE id = %s
        """, (job_id,))
    
    row = cursor.fetchone()
    title = row[0]
    description = row[1]

    cursor.execute("""
        insert into projects (title, description)
        values (%s, %s)
        """, (title, description))
    
    connection.commit()

    cursor.close()
    connection.close()
    
    return redirect(url_for('admin.home'))

@admin_bp.route('/assigned_project/') 
def assignedProjects():
    if 'user_id' not in session:
        return redirect(url_for('main.login'))

    if session['role_id'] == 2:
        return redirect(url_for('projectManagers.home'))
    elif session['role_id'] == 3:
        return redirect(url_for('teamMembers.home'))
    
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        select p.id, p.description, u.name, p.start_date, p.deadline, p.progress
        from projects p
        join users u
        on p.manager_id = u.id
        where manager_id is not null
    """)

    projects = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('admin_pages/admin_assignedProjects.html', projects = projects)

@admin_bp.route('/jobHistory/') 
def jobHistory():
    if 'user_id' not in session:
        return redirect(url_for('main.login'))

    if session['role_id'] == 2:
        return redirect(url_for('projectManagers.home'))
    elif session['role_id'] == 3:
        return redirect(url_for('teamMembers.home'))

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        select id, title, job_description, proposal, feasibility, approval
        from job_proposal
        where status = 'inactive'
        """)
    
    jobs = cursor.fetchall()

    return render_template('admin_pages/admin_job_history.html', jobs=jobs)

@admin_bp.route('/profile/') 
def profile():
    if 'user_id' not in session:
        return redirect(url_for('main.login'))

    if session['role_id'] == 2:
        return redirect(url_for('projectManagers.home'))
    elif session['role_id'] == 3:
        return redirect(url_for('teamMembers.home'))
    
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        select u.id, u.name, u.email, r.title
        from users u
        join roles r
        on u.role_id = r.id 
        where u.id = %s
    """,(session['user_id'],))

    profile = cursor.fetchone()

    cursor.close()
    connection.close()

    return render_template('admin_pages/admin_profile.html', profile = profile)