from flask import Blueprint, render_template, request, redirect, url_for, session
from app.db import get_connection
from datetime import datetime

projectManagers_bp = Blueprint('projectManagers', __name__, url_prefix='/projectManagers')

@projectManagers_bp.route('/')
def home():
    if 'user_id' not in session:
        return redirect(url_for('main.login'))

    if session['role_id'] == 1:
        return redirect(url_for('admin.home'))
    elif session['role_id'] == 3:
        return redirect(url_for('teamMember.home'))

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        select id, start_date, deadline, title, description, progress
        from projects
        where manager_id = %s
    """,(session['user_id'],))

    projects = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('projectManagers_pages/pm_home.html', projects=projects)
