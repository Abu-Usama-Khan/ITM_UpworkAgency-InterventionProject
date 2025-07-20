from flask import Blueprint, render_template, request, redirect, url_for, session
from app.db import get_connection

teamMembers_bp = Blueprint('teamMembers', __name__, url_prefix='/teamMembers')